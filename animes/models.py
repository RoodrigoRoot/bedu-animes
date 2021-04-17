from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Anime(models.Model):
    title = models.CharField(max_length=250, verbose_name="Name")
    episodes = models.CharField(max_length=100)
    start_airing =  models.CharField(max_length=100)
    end_airing =  models.CharField(max_length=100)
    starting_season = models.CharField(max_length=100)
    broadcast_time =  models.CharField(max_length=100)
    licensors = models.TextField()
    producers =  models.TextField()
    studios = models.CharField(max_length=50)
    sources = models.CharField(max_length=50)
    genres = models.TextField()
    duration = models.CharField(max_length=100)
    rating =  models.CharField(max_length=10)
    score = models.FloatField()
    score_by = models.IntegerField()
    members = models.IntegerField()
    favorites = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ["-title"]