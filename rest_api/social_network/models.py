from django.db import models
from django.contrib.auth.models import User



class Post(models.Model):
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    body = models.CharField(blank=True, max_length=250)
    # like = models.PositiveSmallIntegerField(null=True)
    likes = models.IntegerField()
    dislikes = models.IntegerField()

class likes(models.Model):
    post = models.ForeignKey(Post, null=True, on_delete=models.CASCADE)
    liker = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    islike = models.BooleanField(default=False)

class LogTime(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

def __str__(self):
        return self.title
