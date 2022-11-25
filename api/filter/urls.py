from django.urls import path, include
from .views import RequestPhotoFilterView

urlpatterns = [path("", RequestPhotoFilterView.as_view()),]
