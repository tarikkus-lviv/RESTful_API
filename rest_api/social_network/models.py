from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(blank=True, max_length=250)
    like = models.PositiveSmallIntegerField()

def __str__(self):
        return self.title
