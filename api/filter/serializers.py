from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *



class MockedSerialiser(serializers.ModelSerializer):
    """Загруженные данные"""

    url = serializers.CharField()
