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
