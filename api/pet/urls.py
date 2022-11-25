from django.urls import path, include
from .views import ProfileView, PetView, PetsListView, RequestPhotoView, RequestPollView, RequestPhotoListView, RequestListPollView

urlpatterns = [path("profile/", ProfileView.as_view()),
               path("pet/", PetView.as_view()),
               path("pet/list/", PetsListView.as_view()),
               path("request/photo/", RequestPhotoView.as_view()),
               path("request/photo/list/", RequestPhotoListView.as_view()),
               path("request/poll/", RequestPollView.as_view()),
               path("request/poll/list/", RequestListPollView.as_view()),
               ]
