import os.path
from django.http import QueryDict
from rest_framework.response import Response
from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser, JSONParser
from rest_framework import viewsets, status, generics, pagination, filters, permissions
from rest_framework.views import APIView
import urllib.parse
from PIL import Image
from django.conf import settings
import requests

from ..models import *
from ..serializers import *

class RequestPhotoView(generics.GenericAPIView):
    """Запрос с фотографией"""

    permission_classes = [permissions.AllowAny]
    serializer_class = RequestPhotoFullSerialiser

    # def post(self, request):
    #     """Отправить 1 фото"""
    #
    #     id = request.POST.get('id')  # id питомца
    #     photo = request.POST.get('photo')
    #
    #     example = {
    #         "id": 1,
    #         "pet": "Пушок",
    #         "photo": "http: //",
    #         "date_creation": 10,
    #     }
    #
    #     return Response(example, status=status.HTTP_200_OK)

    def post(self, request):
        """Получение данных и описания"""
        # парсим запрос
        pet_id = request.data.get('id') # id
        file = request.data.get('file')  # file

        current_user = request.user
        if not Pet.objects.filter(pk=pet_id).exists():
            massage = f"Пользователь {current_user} еще не имеет питомца с id={pet_id}"
            return Response(massage, status=status.HTTP_404_NOT_FOUND)

        pet = Pet.objects.get(id=pet_id)

        # если не передали файл в запросе
        if not file:
            raise ParseError("Empty content")

        # проверка формата файла
        try:
            img = Image.open(file)
            img.verify()
        except:
            raise ParseError("Unsupported image type")

        # сохранение файла в БД
        request_photo = RequestPhoto(photo=file, pet=pet)
        request_photo.switch_status("received")
        request_photo.save()

        serializer = RequestPhotoUrlSerialiser(request_photo)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


    def get(self, request):
        """Информация 1го запроса"""

        # example = {
        #     "id": 1,
        #     "pet": "Пушок",
        #     "photo": "http: //",
        #     "date_creation": '22-11-22:10:10',
        #     "prediction": {
        #         'red': True,
        #         "ensects": True
        #     }
        # }

        id = request.GET.get('id')
        current_user = request.user

        if not RequestPhoto.objects.filter(pk=id).exists():
            massage = f"Пользователь {current_user} еще не имеет запрос с id={id}"
            return Response(massage, status=status.HTTP_404_NOT_FOUND)

        request_photo = RequestPhoto.objects.get(pk=id)
        serializer = RequestPhotoUrlSerialiser(request_photo)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):

        id = request.GET.get('id')
        current_user = request.user

        if not RequestPhoto.objects.filter(pk=id).exists():
            massage = f"Пользователь {current_user} не имеет запрос с id={id}"
            return Response(massage, status=status.HTTP_404_NOT_FOUND)

        request_photo = RequestPhoto.objects.get(pk=id) # instance
        # удалить изображение
        request_photo.photo.delete(save=False)
        # удалить весь запрос
        request_photo.delete()

        return Response(f"Request with id={id} has been deleted", status=status.HTTP_200_OK)

class RequestPhotoListView(generics.GenericAPIView):
    """Список запросов с фотографиями"""

    permission_classes = [permissions.AllowAny]
    serializer_class = RequestPhotoFullSerialiser

    def get(self, request):
        """Получить"""

        pet_id = request.data.get('id')  # id питомца
        current_user = request.user

        if not Pet.objects.filter(pk=pet_id).exists():
            massage = f"Пользователь {current_user} еще не имеет питомца с id={pet_id}"
            return Response(massage, status=status.HTTP_404_NOT_FOUND)

        pet = Pet.objects.get(id=pet_id)
        pet_list = RequestPhoto.objects.filter(pet=pet) # все запросы для конкретного питомца
        serializer = RequestPhotoUrlSerialiser(pet_list, many=True)

        # example = {'list': [
        #     {"id": 1,
        #      "pet": "Пушок",
        #      "photo": "http: //",
        #      "date_creation": '22-11-22:10:10',
        #      "prediction": {
        #          'red': True,
        #          "ensects": True
        #      }},
        #     {"id": 1,
        #      "pet": "Пушок",
        #      "photo": "http: //",
        #      "date_creation": '22-11-22:10:10',
        #      "prediction": {
        #          'red': True,
        #          "ensects": True
        #      }}]
        # }

        return Response(serializer.data, status=status.HTTP_200_OK)



class RequestPhotoFilterView(generics.GenericAPIView):
    """Отправить полученное фото на фильтр"""

    permission_classes = [permissions.AllowAny]
    serializer_class = RequestPhotoFullSerialiser

    def post(self, request):
        """Отправить 1 фото"""

        # принимаем данные
        id_request = request.POST.get('id') # id запроса
        current_user = request.user

        # получаем запрос и достаем url фотки
        if not RequestPhoto.objects.filter(pk=id_request).exists():
            massage = f"Пользователь {current_user} еще не имеет запроса с id={id_request}"
            return Response(massage, status=status.HTTP_404_NOT_FOUND)
        current_request = RequestPhoto.objects.get(pk=id_request)

        # проверка входных данных
        serializer = MicroserviceIdSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # прогоним через сериалазер чтоб получить полный url
        serializer = RequestPhotoUrlSerialiser(current_request)
        url = serializer.data.get("photo")

        # запрос на микросервис
        response = requests.post(settings.FILTER_URL, data={'url': url, 'id': id_request}).json()

        # обработали данные  с фильтра и достали тип
        # TODO unused - логика обработки будет на фронте или в таблицу запишем?
        serializer_data = FilterSerialiser(response.get("filter")).data
        type = serializer_data["type"]

        # меняем статус
        current_request.switch_status("filter")

        # example = {
        #     "type": "poop"
        # }

        return Response(response, status=status.HTTP_200_OK)


class RequestPhotoPredictionView(generics.GenericAPIView):
    """Отправить полученное фото на предсказание"""

    permission_classes = [permissions.AllowAny]
    serializer_class = RequestPhotoFullSerialiser

    def post(self, request):
        """Отправить 1 фото"""

        # принимаем данные
        id_request = request.POST.get('id') # id запроса
        current_user = request.user

        # проверка входных данных
        serializer = MicroserviceIdSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # получаем запрос и достаем url фотки
        if not RequestPhoto.objects.filter(pk=id_request).exists():
            massage = f"Пользователь {current_user} еще не имеет запроса с id={id_request}"
            return Response(massage, status=status.HTTP_404_NOT_FOUND)
        current_request = RequestPhoto.objects.get(pk=id_request)

        # прогоним через сериалазер чтоб получить полный url
        serializer = RequestPhotoUrlSerialiser(current_request)
        url = serializer.data.get("photo")

        # запрос на микросервис
        response = requests.post(settings.PREDICTOR_URL, data={'url': url, 'id': id_request}).json()
        current_request.switch_status("predictor")

        # парсим запрос и добавляем болезни в таблицу
        predictor_serializer_data = PredictorSerialiser(response.get("predictor")).data
        for key, value in predictor_serializer_data.items():
            if value:
                disease = Diseases.objects.get(label=key)
                current_request.diseases.add(disease)

        # меняем статус запроса
        if id_request:
            if not RequestPhoto.objects.filter(pk=id_request).exists():
                massage = f"Пользователь {current_user} еще запроса с id={id_request}"
                return Response(massage, status=status.HTTP_404_NOT_FOUND)
            RequestPhoto.objects.get(pk=id_request).switch_status("predictor")

        # example = {
        #     "blood": True,
        #     "parasites": False
        # }

        # отдаем весь запрос TODO сделать в виде списка болезней!
        request_serializer_data = RequestPhotoUrlSerialiser(current_request).data

        return Response(request_serializer_data, status=status.HTTP_200_OK)


class QuickPhotoPredictionView(generics.GenericAPIView):
    """Быстрая проверка фотки"""

    permission_classes = [permissions.AllowAny]
    serializer_class = RequestPhotoFullSerialiser

    def post(self, request):
        """Отправить 1 фото"""

        # получаем фото
        file = request.data.get('file')  # file

        # проверка
        if not file:
            raise ParseError("Empty content")

        # открытие
        try:
            img = Image.open(file)
            img.verify()
        except:
            raise ParseError("Unsupported image type")

        # cохраняем в БД
        current_request = QuickRequestPhoto(photo=file)
        current_request.switch_status("received")
        current_request.save()

        # достаем id запроса
        id_request = current_request.id

        # достаем URL
        serializer = QuickRequestPhotoUrlSerialiser(current_request)
        url = serializer.data.get("photo")

        # отправляем на сервис-1
        response_filter = requests.post(settings.FILTER_URL, data={'url': url, 'id': id_request}).json()
        current_request.switch_status("filter")

        # отправляем на сервис-2
        response_predictor = requests.post(settings.PREDICTOR_URL, data={'url': url, 'id': id_request}).json()
        current_request.switch_status("predictor")

        # парсим запрос и добавляем болезни в таблицу
        predictor_serializer_data = PredictorSerialiser(response_predictor.get("predictor")).data
        for key, value in predictor_serializer_data.items():
            if value:
                disease = Diseases.objects.get(label=key)
                current_request.diseases.add(disease)

        # получаем список болезней
        diseases_list = current_request.diseases.all()
        diseases_serializer_data = DiseasesFullSerialiser(diseases_list, many=True).data

        # собираем ответ
        # response = {"filter": response_filter, "predictor": response_predictor}

        # удаляем фото из БД
        current_request.photo.delete(save=False)
        current_request.delete()

        # отдаем ответ в виде списка болезней
        return Response(diseases_serializer_data, status=status.HTTP_200_OK)


class RequestPhotoDiseasesView(generics.GenericAPIView):

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        id = request.GET.get('id')
        current_user = request.user

        if not RequestPhoto.objects.filter(pk=id).exists():
            massage = f"Пользователь {current_user} еще не имеет запрос с id={id}"
            return Response(massage, status=status.HTTP_404_NOT_FOUND)

        request_photo = RequestPhoto.objects.get(pk=id)
        diseases_list = request_photo.diseases.all()
        serializer = DiseasesFullSerialiser(diseases_list, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)