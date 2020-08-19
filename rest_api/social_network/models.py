from django.db import models
from django.contrib.auth.models import User



class Post(models.Model):
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    body = models.CharField(blank=True, max_length=250)
    likes = models.ManyToManyField(User, blank=True, related_name='post_likes')

    def __str__(self):
        return self.title

class Like(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, null=True, on_delete=models.CASCADE)
    value = models.ManyToManyField(User, blank=True, related_name='value_likes')

    def __str__(self):
        return str(self.post)
