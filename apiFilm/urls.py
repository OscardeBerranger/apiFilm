from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from movie.views import MovieList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('movie.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]