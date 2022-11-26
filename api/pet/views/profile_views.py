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

class ProfileListView(generics.ListAPIView):
    """Все профили"""

    permission_classes = [permissions.AllowAny]
    queryset = Profile.objects.all()
    serializer_class = ProfileFullSerialiser

class ProfileView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        """Получить профиль пользователя"""

        #         example = {
        #             "first_name": "Дмитрий",
        #             "second_name": "Алексеевич",
        #             "last_name": "Борисов",
        #             "avatar": "https://pixelbox.ru/wp-content/uploads/2021/02/mult-ava-instagram-69.jpg",
        #             'active': True
        #         }

        current_user = request.user

        if not Profile.objects.filter(user=current_user).exists():
            massage = f"Пользователь {current_user} еще не создал профиль"
            return Response(massage, status=status.HTTP_404_NOT_FOUND)

        current_profile = Profile.objects.get(user=current_user)
        serializer = ProfileFullSerialiser(current_profile)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """Соаздать профиль"""

        # добавляем владелька к профилю
        if isinstance(request.data, QueryDict):  # optional
            request.data._mutable = True
        current_user = request.user
        request.data.update({"user": current_user.id})

        serializer = ProfileFullSerialiser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_200_OK)