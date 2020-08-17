from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model

class Post(models.Model):
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    # author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    body = models.CharField(blank=True, max_length=250)
    like = models.PositiveSmallIntegerField()

def __str__(self):
        return self.title
