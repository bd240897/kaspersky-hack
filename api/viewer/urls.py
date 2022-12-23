from django.urls import path
from .views import QuickStartView

urlpatterns = [path('quick/', QuickStartView.as_view(), name='quick'),]