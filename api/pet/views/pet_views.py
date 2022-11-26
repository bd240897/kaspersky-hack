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


class PetView(generics.GenericAPIView):
    """Питомец"""

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PetFullSerialiser

    def post(self, request):
        """Добавить питомца"""

        # example = {'massage': "Данные питомца успешно обновлены"}

        if isinstance(request.data, QueryDict):  # optional
            request.data._mutable = True
        current_user = request.user
        request.data.update({"user": current_user.id})

        serializer = PetFullSerialiser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_200_OK)

    # https://stackoverflow.com/questions/62099191/genericapiview-should-either-include-a-serializer-class-attribute-or-override
    def get(self, request):
        """Получить данные 1го питомца"""

        # example = {
        #     "id": 1,
        #     "owner": "Дима",
        #     "avatar": "https://pixelbox.ru/wp-content/uploads/2021/02/mult-ava-instagram-69.jpg",
        #     "age": 10,
        #     "weight": 20,
        #     "breed": "Овчарка",
        #     "name": "Пушок",
        # }

        id = request.GET.get('id')
        current_user = request.user

        if not Pet.objects.filter(pk=id, user=current_user).exists():
            massage = f"Пользователь {current_user} еще не имеет питомца с id={id}"
            return Response(massage, status=status.HTTP_404_NOT_FOUND)

        current_pet = Pet.objects.get(pk=id, user=current_user)
        serializer = PetFullSerialiser(current_pet)
        return Response(serializer.data, status=status.HTTP_200_OK)


# class PetsListView(generics.GenericAPIView):
#     """Питомцы"""
#
#     permission_classes = [permissions.AllowAny]
#
#     def get(self, request):
#         """Получить список питомцев пользователя"""
#
#         example = {"list": [
#             {
#                 "id": 1,
#                 "name": "Пушок",
#             },
#             {
#                 "id": 2,
#                 "name": "Беляш",
#             }]
#         }
#
#         return Response(example, status=status.HTTP_200_OK)


class PetsListView(generics.ListAPIView):
    """Список моих питомцев"""

    model = Pet
    serializer_class = PetFullSerialiser
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Pet.objects.filter(user=self.request.user)
        return queryset


