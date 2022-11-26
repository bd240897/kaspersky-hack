from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, Pet, Diseases, RequestPoll, RequestPhoto, QuickRequestPhoto
from django.conf import settings

class ProfileFullSerialiser(serializers.ModelSerializer):
    """Загруженные данные"""

    class Meta:
        model = Profile
        fields = "__all__" # ('id', 'first_name', 'second_name', 'third_name', 'avatar', 'active', 'date_creation',)


class PetFullSerialiser(serializers.ModelSerializer):
    """Загруженные данные"""

    class Meta:
        model = Pet
        fields = "__all__"

class DiseasesFullSerialiser(serializers.ModelSerializer):
    """Загруженные данные"""

    class Meta:
        model = Diseases
        fields = "__all__"

class RequestPhotoFullSerialiser(serializers.ModelSerializer):
    """Загруженные данные"""

    class Meta:
        model = RequestPhoto
        fields = "__all__"

class RequestPhotoUrlSerialiser(serializers.ModelSerializer):
    """Данные запроса + правильный URL"""

    photo = serializers.SerializerMethodField()

    def get_photo(self, obj):
        return settings.HOST_URL + obj.photo.url

    class Meta:
        model = RequestPhoto
        fields = "__all__"


class RequestPollFullSerialiser(serializers.ModelSerializer):
    """Загруженные данные"""

    class Meta:
        model = RequestPoll
        fields = "__all__"


class QuickRequestPhotoUrlSerialiser(serializers.ModelSerializer):
    """Данные запроса + правильный URL"""

    photo = serializers.SerializerMethodField()

    def get_photo(self, obj):
        return settings.HOST_URL + obj.photo.url

    class Meta:
        model = QuickRequestPhoto
        fields = "__all__"


class MicroserviceIdSerializer(serializers.Serializer):
    """Данные для нейронок"""

    id = serializers.CharField() # id request

class MicroserviceFullSerializer(serializers.Serializer):
    """Данные для нейронок"""

    url = serializers.CharField() # url photo
    id = serializers.CharField() # id request


# class ProfileSerialiser(serializers.ModelSerializer):
#     """Загруженные данные"""
#
#     class Meta:
#         model = Profile
#         fields = ('id', 'first_name', 'second_name', 'third_name', 'avatar', 'active', 'date_creation',)
#
#
# class CurrencySerialiser(serializers.ModelSerializer):
#     """Загруженные данные"""
#
#     class Meta:
#         model = Currency
#         fields = ('id', 'name', 'country',)
#
#
# class CurrencyCourseSerialiser(serializers.ModelSerializer):
#     """Загруженные данные"""
#
#     currency = serializers.SerializerMethodField()
#
#     class Meta:
#         model = CurrencyCourse
#         fields = ('id', 'first_name', 'course_cb', 'date', 'currency',)
#
#     def get_currency(self, obj):
#         return obj.currency.name
#
#
# class WalletSerialiser(serializers.ModelSerializer):
#     """Загруженные данные"""
#
#     currency = serializers.SerializerMethodField()
#
#     class Meta:
#         model = Wallet
#         fields = "__all__"
#
#     def get_currency(self, obj):
#         return obj.currency.name
#
# class WalletListSerialiser(serializers.ModelSerializer):
#     """Загруженные данные"""
#
#     currency = serializers.SerializerMethodField()
#
#     class Meta:
#         model = Wallet
#         fields = ('id', 'name', 'currency', 'value')
#
#     def get_currency(self, obj):
#         return obj.currency.name
#
#
# class TransferSerialiser(serializers.ModelSerializer):
#     """Загруженные данные"""
#
#     from_account_currency = serializers.SerializerMethodField()
#     to_account_currency = serializers.SerializerMethodField()
#
#     class Meta:
#         model = Transfer
#         fields = ('from_account', 'to_account', "value", "date", "from_account_currency", 'owner', "to_account_currency") # ,
#
#     def get_from_account_currency(self, obj):
#         return obj.from_account.currency.name
#
#     def get_to_account_currency(self, obj):
#         return obj.to_account.currency.name
#
#
# class FullTransferSerialiser(TransferSerialiser):
#     from_account_name = serializers.SerializerMethodField()
#     to_account_name = serializers.SerializerMethodField()
#     currency = serializers.SerializerMethodField()
#
#     class Meta:
#         model = Transfer
#         fields = ('currency', 'value', 'from_account_id', 'to_account_id', 'from_account_name', 'to_account_name',
#                   'currency', 'id', 'date')
#
#     def get_from_account_name(self, obj):
#         return obj.from_account.name
#
#     def get_to_account_name(self, obj):
#         return obj.to_account.name
#
#     def get_currency(self, obj):
#         return obj.currency.name