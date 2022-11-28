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
    """Болезни данные"""

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
    # diseases = DiseasesFullSerialiser()

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


class FilterSerialiser(serializers.Serializer):
    """Обрабатываем данные с фильтра"""

    type = serializers.CharField()

class PredictorSerialiser(serializers.Serializer):
    """Обрабатываем данные с предсказателя"""

    blood = serializers.BooleanField()
    parasite = serializers.BooleanField()
