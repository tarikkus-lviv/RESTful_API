from django.contrib import admin
from .models import Post, LogTime, likes

admin.site.register(Post)
admin.site.register(likes)

admin.site.register(LogTime)
