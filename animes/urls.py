from django.urls import path
from .views import AnimeListCreateAPIView

urlpatterns = [
    path("animes/", AnimeListCreateAPIView.as_view()),
]
