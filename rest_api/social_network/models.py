from django.db import models
from django.contrib.auth.models import User



class Post(models.Model):
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    body = models.CharField(blank=True, max_length=250)
    likes = models.ManyToManyField(User, blank=True, related_name='post_likes')

def __str__(self):
        return self.title
