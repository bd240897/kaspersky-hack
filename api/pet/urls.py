from django.http import HttpResponse
from django.urls import path, include

from .views.request_photo_views import QuickPhotoPredictionView, RequestPhotoDiseasesView
from .views.views import ProfileView, PetView, PetsListView, RequestPhotoView, RequestPollView, RequestPhotoListView, \
    RequestListPollView, ProfileListView, RequestPhotoFilterView, RequestPhotoPredictionView

urlpatterns = [path("profile/", ProfileView.as_view()),
               path("profile/list/", ProfileListView.as_view()),
               path("pet/", PetView.as_view()),
               path("pet/list/", PetsListView.as_view()),

               # запрос с фото
               path("request/photo/", RequestPhotoView.as_view()),
               path("request/photo/filter/", RequestPhotoFilterView.as_view()),  # отравить запро на фильтр
               path("request/photo/predictor/", RequestPhotoPredictionView.as_view()),  # отравить запро на фильтр
               path("request/photo/list/", RequestPhotoListView.as_view()),
               path("request/photo/diseases/", RequestPhotoDiseasesView.as_view()),

               # запрос с опросом
               path("request/poll/", RequestPollView.as_view()),
               path("request/poll/list/", RequestListPollView.as_view()),

               # быстрый запрос
               path("request/photo/quick/", QuickPhotoPredictionView.as_view()),
               ]
