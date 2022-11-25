import os.path

from django.http import QueryDict
from rest_framework.response import Response
from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser, JSONParser
from rest_framework import viewsets, status, generics, pagination, filters, permissions
from rest_framework.views import APIView
import urllib.parse
from PIL import Image
from .models import Profile, Wallet, Transfer
from .serializers import WalletSerialiser, ProfileSerialiser, TransferSerialiser, WalletListSerialiser
from django.conf import settings

class ProfileView(generics.GenericAPIView):
    """Профиль"""

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        """Отправка ссылки на файл (необработанный)"""

        current_user = request.user

        # example = {
        #     "first_name": "Дмитрий",
        #     "second_name": "Алексеевич",
        #     "last_name": "Борисов",
        #     "avatar": "https://pixelbox.ru/wp-content/uploads/2021/02/mult-ava-instagram-69.jpg",
        #     'active': True
        # }

        return Response(serializer.data, status=status.HTTP_200_OK)