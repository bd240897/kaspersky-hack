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

class RequestPhotoFilterView(generics.GenericAPIView):
    """Отправить полученное фото на фильтр"""

    permission_classes = [permissions.AllowAny]
    serializer_class = MockedSerialiser

    def post(self, request):
        """Отправить 1 фото"""

        url = request.POST.get('url')  # id питомца

        # TODO тут он изменяет статус на

        example = {
            "type": "poop"
        }

        return Response(example, status=status.HTTP_200_OK)