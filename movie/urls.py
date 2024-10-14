from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, MovieList

router = DefaultRouter()
router.register(r'movie', MovieViewSet)

urlpatterns = [
    path('create/movie', MovieViewSet.as_view({'post': 'create'})),
    path('get/movie', MovieList.as_view()),
]