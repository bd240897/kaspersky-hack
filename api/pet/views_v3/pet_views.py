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


class PetViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PetFullSerialiser
    queryset = Pet.objects.all()

    def retrieve(self, request, *args, **kwargs):
        """Данные о питомце"""

        id = kwargs.get('pk')
        current_user = request.user
        if not Pet.objects.filter(pk=id, user=current_user).exists():
            massage = f"Пользователь {current_user} еще не имеет питомца с id={id}"
            return Response(massage, status=status.HTTP_404_NOT_FOUND)

        return super().retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """Создание"""

        # добавим пользователя к request.data
        if isinstance(request.data, QueryDict):  # optional
            request.data._mutable = True
        current_user = request.user
        request.data.update({"user": current_user.id})
        return super().create(request, *args, **kwargs)

    def get_queryset(self):
        if self.action == 'list':
            return Pet.objects.filter(user=self.request.user)
        return super().get_queryset()

    def list(self, request, *args, **kwargs):
        """Список"""
        # query_set определен выше чтоб вывести только моих питомцев
        return super().list( request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """Обновить"""

        id = kwargs.get('pk')
        current_user = request.user
        if not Pet.objects.filter(pk=id, user=current_user).exists():
            massage = f"Питомец id={id} не принадлежит текущему юзеру {current_user}!"
            return Response(massage, status=status.HTTP_404_NOT_FOUND)

        # добавим пользователя к request.data
        if isinstance(request.data, QueryDict):  # optional
            request.data._mutable = True
        current_user = request.user
        request.data.update({"user": current_user.id})
        return super().update(request, *args, **kwargs)




# сделать 2 функции
# pet/instance/
# get_one, delete, update
# pet/
# list, crate
