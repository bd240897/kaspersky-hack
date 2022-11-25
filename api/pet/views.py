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

from .models import *
from .serializers import *

"api/v1/profile/"


class ProfileView(generics.GenericAPIView):
    """Профиль"""

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        """Получить профиль пользователя"""

        example = {
            "first_name": "Дмитрий",
            "second_name": "Алексеевич",
            "last_name": "Борисов",
            "avatar": "https://pixelbox.ru/wp-content/uploads/2021/02/mult-ava-instagram-69.jpg",
            'active': True
        }

        return Response(example, status=status.HTTP_200_OK)


"api/v1/pet/"


class PetView(generics.GenericAPIView):
    """Питомцы"""

    permission_classes = [permissions.AllowAny]
    serializer_class = PetFullSerialiser

    # https://stackoverflow.com/questions/62099191/genericapiview-should-either-include-a-serializer-class-attribute-or-override

    def get(self, request):
        """Получить список питомцев пользователя"""

        id = request.POST.get('id')
        # TODO

        example = {
            "id": 1,
            "owner": "Дима",
            "avatar": "https://pixelbox.ru/wp-content/uploads/2021/02/mult-ava-instagram-69.jpg",
            "age": 10,
            "weight": 20,
            "breed": "Овчарка",
            "name": "Пушок",
        }
        return Response(example, status=status.HTTP_200_OK)

    def post(self, request):
        """Получить список питомцев пользователя"""

        # data = request.POST

        example = {'massage': "Данные питомца успешно обновлены"}

        return Response(example, status=status.HTTP_200_OK)


"api/v1/pet/list/"


class PetsListView(generics.GenericAPIView):
    """Питомцы"""

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        """Получить список питомцев пользователя"""

        example = {"list": [
            {
                "id": 1,
                "name": "Пушок",
            },
            {
                "id": 2,
                "name": "Беляш",
            }]
        }

        return Response(example, status=status.HTTP_200_OK)


# TODO - запросы сделать в виде отдельной табличики
#
# Питомец
#
# Запросы
# FK Pet
#
# Предсказания
# FK Request

"api/v1/send/photo"


class RequestPhotoView(generics.GenericAPIView):
    """Запрос с фотографией"""

    permission_classes = [permissions.AllowAny]
    serializer_class = RequestPhotoFullSerialiser

    def post(self, request):
        """Отправить 1 фото"""

        id = request.POST.get('id')  # id питомца
        photo = request.POST.get('photo')

        example = {
            "id": 1,
            "pet": "Пушок",
            "photo": "http: //",
            "date_creation": 10,
        }

        return Response(example, status=status.HTTP_200_OK)

    def get(self, request):
        """Информация 1го запроса"""

        id = request.POST.get('id')  # id питомца

        example = {
            "id": 1,
            "pet": "Пушок",
            "photo": "http: //",
            "date_creation": '22-11-22:10:10',
            "prediction": {  # TODO
                'red': True,
                "ensects": True
            }
        }

        return Response(example, status=status.HTTP_200_OK)


class RequestPhotoListView(generics.GenericAPIView):
    """Список запросов с фотографиями"""

    permission_classes = [permissions.AllowAny]
    serializer_class = RequestPhotoFullSerialiser

    def get(self, request):
        """Получить"""

        id = request.POST.get('id')  # id питомца

        example = {'list': [
            {"id": 1,
             "pet": "Пушок",
             "photo": "http: //",
             "date_creation": '22-11-22:10:10',
             "prediction": {
                 'red': True,
                 "ensects": True
             }},
            {"id": 1,
             "pet": "Пушок",
             "photo": "http: //",
             "date_creation": '22-11-22:10:10',
             "prediction": {
                 'red': True,
                 "ensects": True
             }}]
        }

        return Response(example, status=status.HTTP_200_OK)


"api/v1/send/poll"


class RequestPollView(generics.GenericAPIView):
    """Запрос с опросом"""

    permission_classes = [permissions.AllowAny]
    serializer_class = RequestPollFullSerialiser

    def post(self, request):
        """Отправить 1 опрос"""

        id = request.POST.get('id')  # id питомца
        data = request.POST.get('data')

        example = {
            "id": 1,
            "pet": "Пушок",
            "date_creation": '22-11-22:10:10',
            "data": {
                "insection": [1, 2, 3],
                "feed": [2, 3],
                "leg": [2, 3],
            },
        }

        # TODO maybe need Json maker

        return Response(example, status=status.HTTP_200_OK)

    def get(self, request):
        """Информация 1го опроса"""

        id = request.POST.get('id')  # id питомца

        example = {
            "id": 1,
            "pet": "Пушок",
            "photo": "http: //",
            "date_creation": 10,
            "data": {
                "insection": [1, 2, 3],
                "feed": [2, 3],
                "leg": [2, 3],
            },
        }

        return Response(example, status=status.HTTP_200_OK)

class RequestListPollView(generics.GenericAPIView):
    """Список запросов с опросами"""

    permission_classes = [permissions.AllowAny]
    serializer_class = RequestPollFullSerialiser

    def get(self, request):
        """Получить"""

        id = request.POST.get('id')  # id питомца

        example = {'list': [
            {"id": 1,
             "pet": "Пушок",
             "photo": "http: //",
             "date_creation": '22-11-22:10:10',
             "prediction": {
                 'red': True,
                 "ensects": True
             }},
            {"id": 1,
             "pet": "Пушок",
             "photo": "http: //",
             "date_creation": '22-11-22:10:10',
             "prediction": {
                 'red': True,
                 "ensects": True
             }}]
        }

        return Response(example, status=status.HTTP_200_OK)
