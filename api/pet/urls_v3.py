from django.http import HttpResponse
from django.urls import path, include
from rest_framework import routers

from .views_v3.views import PetViewSet

router = routers.DefaultRouter()
router.register(r'pet', PetViewSet)

urlpatterns = [path("", include(router.urls)),]


