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

# это моя нейронка
from .ml_models.blood_alexnet.BaselineClass import BaseLine as Blood_baseline
from .ml_models.parasites_alexnet.BaselineClass import BaseLine as Parasites_baseline



def blood_cnn(url):
    """Предсказание крови"""

    # подгружаем модель
    model = Blood_baseline()

    # делаем предсказание и ловим исключения в случае ошибки модели
    prediction = model.predict_file(url=url)

    # получаем ответ
    answer = {"blood": prediction}
    return answer


def parasite_cnn(url):
    """Предсказание паразитов"""

    # подгружаем модель
    model = Parasites_baseline()

    # делаем предсказание
    prediction = model.predict_file(url=url)

    # получаем ответ
    answer = {"parasite": prediction}
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

        # проверки
        if not url:
            return Response("Вы не передали URL картинки!", status=status.HTTP_400_BAD_REQUEST)

        # вызываем сетки
        try:
            answer_parasite_cnn = parasite_cnn(url)
            answer_blood_cnn = blood_cnn(url)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

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
