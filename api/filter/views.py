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
from .ml_alexnet.BaselineClass import BaseLine

class RequestPhotoFilterView(generics.GenericAPIView):
    """Отправить полученное фото на фильтр"""

    permission_classes = [permissions.AllowAny]
    serializer_class = MockedSerialiser

    def post(self, request):
        """Отправить 1 фото"""

        # входные параметры
        url = request.POST.get('url')  # url картинки
        id = request.POST.get('id') # id запроса

        # предсказание нейронки
        model = BaseLine()
        prediction = model.predict_file(url=url)

        example = {
            "filter": {"type": prediction},
            "meta_info": {"id": id, "url": url}
        }

        return Response(example, status=status.HTTP_200_OK)


class FilterOnUrl(generics.GenericAPIView):

    def get(self, request, *args,  **kwargs):

        url = request.GET.get('url')
        if not url:
            return Response("Вы не передали URL картинки!", status=status.HTTP_400_BAD_REQUEST)
        try:
            model = BaseLine()
            prediction = model.predict_file(url=url)
            print(prediction)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

        return Response({"prediction": prediction})



