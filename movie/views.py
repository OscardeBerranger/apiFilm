from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import viewsets, generics, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Movie, Author, Genre, CustomUser
from .serializers import MovieSerializer, AuthorSerializer, RegisterSerializer, GenreSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class documentation(TemplateView):
     template_name = "../templates/documentation.html"

class MovieUpdateView(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]
    def perform_update(self, serializer):
        movie = self.get_object()
        if movie.creator != self.request.user:
            raise PermissionDenied("Vous n'avez pas la permission d'éditer ce film")
        serializer.save()


class MovieDeleteView(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]
    def perform_destroy(self, serializer):
        movie = self.get_object()
        if movie.creator != self.request.user:
            raise PermissionDenied("Vous n'avez pas la permission de supprimer ce film")
        serializer.save()


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAuthenticated]

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer


class LoginView(generics.GenericAPIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response({'error': 'Invalid Credentials'}, status=400)