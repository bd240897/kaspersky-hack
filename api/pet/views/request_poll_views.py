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