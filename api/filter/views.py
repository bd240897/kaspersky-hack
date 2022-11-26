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

# TODO нужны ли эти зависимости?
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

# это моя нейронка
from .ml_models.ml_alexnet.BaselineClass import BaseLine

class RequestPhotoFilterView(generics.GenericAPIView):
    """Отправить полученное фото на фильтр"""

    permission_classes = [permissions.AllowAny]
    serializer_class = MockedSerialiser

    def post(self, request):
        """Отправить 1 фото"""

        # входные параметры
        url = request.POST.get('url')  # url картинки
        id = request.POST.get('id') # id запроса

        # проверки
        if not url:
            return Response("Вы не передали URL картинки!", status=status.HTTP_400_BAD_REQUEST)

        # предсказание нейронки
        model = BaseLine()

        # делаем предсказание и ловим исключения в случае ошибки модели
        try:
            prediction = model.predict_file(url=url)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

        example = {
            "filter": {"type": prediction},
            "meta_info": {"id": id, "url": url}
        }

        return Response(example, status=status.HTTP_200_OK)


