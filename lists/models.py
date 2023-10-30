from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class List(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    character_list = models.TextField()

class CharacterProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    character = models.CharField(max_length=1)
    times_seen = models.IntegerField()
    times_correct = models.IntegerField()