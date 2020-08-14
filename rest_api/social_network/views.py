from django.views.generic import ListView
from django.shortcuts import render
from .models import Post

class PostView(ListView):
    model = Post

    template_name = 'social_network/posts.html'
