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

        serializer = RequestPhotoFullSerialiser(request_photo)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


    def get(self, request):
        """Информация 1го запроса"""

        id = request.POST.get('id')  # id запроса

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
            massage = f"Пользователь {current_user} еще не имеет питомца с id={id}"
            return Response(massage, status=status.HTTP_404_NOT_FOUND)

        request_photo = RequestPhoto.objects.get(pk=id)
        serializer = RequestPhotoFullSerialiser(request_photo)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RequestPhotoListView(generics.GenericAPIView):
    """Список запросов с фотографиями"""

    permission_classes = [permissions.AllowAny]
    serializer_class = RequestPhotoFullSerialiser

    def get(self, request):
        """Получить"""

        pet_id = request.data.get('id')  # id питомца
        pet_id = 1
        current_user = request.user

        if not Pet.objects.filter(pk=pet_id).exists():
            massage = f"Пользователь {current_user} еще не имеет питомца с id={pet_id}"
            return Response(massage, status=status.HTTP_404_NOT_FOUND)

        pet = Pet.objects.get(id=pet_id)


        pet_list = RequestPhoto.objects.filter(pet=pet) # все запросы для конкретного питомца

        serializer = RequestPhotoFullSerialiser(pet_list, many=True)

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

        url = request.POST.get('url')  # id питомца
        # FILTER_URL = 'http://127.0.0.1:8000/api/filter/'
        # запрос на микросервис
        response = requests.post(settings.FILTER_URL, data={'url': 'http://example.com'}).json()

        #
        # # TODO тут он изменяет статус на
        #
        # example = {
        #     "type": "poop"
        # }

        return Response(response, status=status.HTTP_200_OK)




# def django_view(request):
#     # get the response from the URL
#     response = requests.get('http://example.com')
#     return HttpResponse(response.text)

class RequestPhotoPredictionView(generics.GenericAPIView):
    """Отправить полученное фото на предсказание"""

    permission_classes = [permissions.AllowAny]
    serializer_class = RequestPhotoFullSerialiser

    def post(self, request):
        """Отправить 1 фото"""

        url = request.POST.get('url')  # id питомца
        # запрос на микросервис
        # PREDICTOR_URL = 'http://127.0.0.1:8000/api/predictor/'
        response = requests.post(settings.PREDICTOR_URL, data={'url': 'http://example.com'}).json()

        # example = {
        #     "blood": True,
        #     "parasites": False
        # }

        return Response(response, status=status.HTTP_200_OK)


