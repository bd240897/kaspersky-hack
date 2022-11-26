from django.shortcuts import render
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


def blood_cnn(url="default_url"):
    answer = {"blood": True}
    return answer


def parasite_cnn(url="default_url"):
    answer = {"parasite": False}
    return answer


class RequestPhotoPredictorView(generics.GenericAPIView):
    """Отправить полученное фото на предсказание"""

    permission_classes = [permissions.AllowAny]
    serializer_class = MockedSerialiser

    def post(self, request):
        """Отправить 1 фото"""

        # получаем данные
        url = request.POST.get('url')  # url картинки
        id = request.POST.get('id') # id запроса

        # вызываем сетки
        answer_blood_cnn = blood_cnn()
        answer_parasite_cnn = parasite_cnn()

        # склеиваем ответы
        full_answer = {**answer_blood_cnn, **answer_parasite_cnn}

        example = {
            "predictor": full_answer,
            "meta_info": {"id": id, "url": url}
        }

        # example = {
        #     "blood": True,
        #     "parasites": False
        # }

        return Response(example, status=status.HTTP_200_OK)
