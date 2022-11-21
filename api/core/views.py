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

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        """Отправка ссылки на файл (необработанный)"""

        current_user = request.user
        current_profile = Profile.objects.get(user=current_user)
        serializer = ProfileSerialiser(current_profile)
        print(serializer.data)

        # example = {
        #     "first_name": "Дмитрий",
        #     "second_name": "Алексеевич",
        #     "last_name": "Борисов",
        #     "avatar": "https://pixelbox.ru/wp-content/uploads/2021/02/mult-ava-instagram-69.jpg",
        #     'active': True
        # }

        return Response(serializer.data, status=status.HTTP_200_OK)


class WalletView(generics.GenericAPIView):
    """Данные по кошельку (счет)"""

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        """Отправка ссылки на файл (необработанный)"""

        # example = {
        #     "id": 1,
        #     "name": "Кошка-жена",
        #     "owner": "Дмитрий",  # 1
        #     "currency": "USD",  #
        #     "value": 10000,
        #     "value_in_ruble": 600000,
        #     'active': True
        # }

        id = request.GET.get('id')
        current_user = request.user
        wallet = Wallet.objects.get(owner=current_user, id=id)
        serializer = WalletSerialiser(wallet)
        return Response(serializer.data)

class WalletListView(generics.GenericAPIView):
    """Список кошельков"""

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        """Отправка ссылки на файл (необработанный)"""

        # example = {"list": [
        #     {
        #         "id": 1,
        #         "name": "Кошка-жена",
        #         "currency": "USD",  #
        #         "value": 10000,
        #     },
        #     {
        #         "id": 2,
        #         "name": "Зарплата",
        #         "currency": "EUR",  #
        #         "value": 100,
        #     }]
        # }

        current_user = request.user
        wallet = Wallet.objects.filter(owner=current_user)
        serializer = WalletListSerialiser(wallet, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

from .currency import get_currency, convert_currency
class TransferCoinView(generics.GenericAPIView):
    """Перевод денег"""

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        """Отправка ссылки на файл (необработанный)"""

        # example = {
        #     "from_account": 1,  # id
        #     "to_account": 2,  # id
        #     "value": 50,
        #     "currency": "USD"
        # }

        # https://stackoverflow.com/questions/33861545/how-can-modify-request-data-in-django-rest-framework
        # добавим пользователя в список request.data - тут он требует добавлять id а не юзер

        # TODO подумать нужен ли юзер тут в этой табличке вообще
        # добавляем владелька к кошельку
        if isinstance(request.data, QueryDict):  # optional
            request.data._mutable = True
        current_user = request.user
        request.data.update({"owner": current_user.id})

        serializer = TransferSerialiser(data=request.data)

        if serializer.is_valid():
            wallet_from = serializer.validated_data.get('from_account') # class 'core.models.Wallet'
            wallet_from_value = wallet_from.value
            wallet_to = serializer.validated_data.get('to_account') # class 'core.models.Wallet'
            wallet_to_value = wallet_to.value
            value = serializer.validated_data.get('value')

            # проверка на кол-во денег
            if wallet_from_value <= value:
                return Response("Не хватает денег!", status=status.HTTP_400_BAD_REQUEST)

            # если кошельки с одинаковой валютой
            if wallet_from.currency == wallet_to.currency:
                wallet_from.value -= value
                wallet_to.value += value
            else:
                converted_value = convert_currency(wallet_from.currency.name,
                                          value,
                                          wallet_to.currency.name)
                wallet_from.value -= value
                wallet_to.value += converted_value

            # сохраняет счета (сумму на них)
            wallet_from.save()
            wallet_to.save()
            # сохраняет историю
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class TransferHistoryView(generics.GenericAPIView):
    """Перевод денег"""

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        """Отправка ссылки на файл (необработанный)"""

        # id = request.POST.get('id')  # id
        #
        # example = {
        #     "date": "10-10-10:21:21",
        #     "from_account_id": 1,  # id
        #     "to_account_id": 2,  # id
        #     "from_account_name": "Зарплата",
        #     "to_account_name": "Кошка-жена",
        #     "value": 50,
        # }

        current_user = request.user
        transfers = Transfer.objects.filter(owner=current_user)
        serializer = TransferSerialiser(transfers, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


# TODO мб не будет использоваться
class GetWalletName(generics.GenericAPIView):
    """Получить имя счета по его id"""

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        """Отправка ссылки на файл (необработанный)"""

        id = request.query_params.get('id') # id

        example = {
                "id": 1,
                "name": "Зарплата",
            }


        return Response(example, status=status.HTTP_200_OK)

# TODO
class CourseView(generics.GenericAPIView):
    """Список кошельков"""

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        """Отправка ссылки на файл (необработанный)"""

        name = request.query_params.get('name') # имя валюты

        example = {"list": [
            {
                "name": "USD",
                "price": "60",  # в рублях
                "type": "Продать",
            },
            {
                "name": "USD",
                "price": "70",  # в рублях
                "type": "Купить",
            }]
        }

        return Response(example, status=status.HTTP_200_OK)

# TODO
class CourseHistoryView(generics.GenericAPIView):
    """История курса"""

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        """Отправка ссылки на файл (необработанный)"""

        name = request.query_params.get('name') # имя валюты

        # TODO
        example = {"list": [
            {
                "1": "1",
            },
            {
                "2": "2",
            }]
        }

        return Response(example, status=status.HTTP_200_OK)


