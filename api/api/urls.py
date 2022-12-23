from django.contrib import admin
from django.urls import path, include, re_path
# для авторизации
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [path('admin/', admin.site.urls),
               # pet
               path("api/v2/", include('pet.urls')),
               path("api/v3/", include('pet.urls_v3')),
               path("viewer/", include('viewer.urls')),
               # cnn
               path("api/filter/", include('filter.urls')),
               path("api/predictor/", include('predictor.urls')),
               # auth
               path('api/v1/drf-auth/', include('rest_framework.urls')),
               path('api/v1/auth/', include('djoser.urls')),
               re_path(r'^auth/', include('djoser.urls.authtoken')),
               ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
