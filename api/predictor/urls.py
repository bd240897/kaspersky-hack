from django.urls import path, include
from .views import RequestPhotoPredictorView

urlpatterns = [path("", RequestPhotoPredictorView.as_view()),]
