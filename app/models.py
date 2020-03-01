from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Animations(models.Model):
    aid = models.IntegerField(primary_key=True)
    title = models.TextField()
    season = models.TextField()

class Abstract(models.Model):
    aid = models.IntegerField(primary_key=True)
    abst_text = models.TextField()

class Review(models.Model):
    aid = models.IntegerField(primary_key=True)
    review_text = models.TextField()

class User_Fav_Anime(models.Model):
    user_name = models.CharField(max_length=64)
    aid = models.IntegerField()
    watch_degree = models.IntegerField()
