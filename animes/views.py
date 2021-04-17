from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .serializers import AnimeSerializer
from .models import Anime
# Create your views here.


class AnimeListCreateAPIView(ListCreateAPIView):
    serializer_class = AnimeSerializer
    queryset = Anime.objects.all()