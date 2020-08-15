from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.CharField(blank=True, max_length=250)
    like = models.PositiveSmallIntegerField()

def __str__(self):
        return self.title
