from rest_framework import generics, authentication
from django.shortcuts import get_object_or_404
from social_network.models import Post, Like
from .serializers import PostSerializer, DetailPostSerializer, PostLikeSerializer
from .permissions import IsAuthorOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response

class PostAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class DetailPostAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = DetailPostSerializer

class PostLikeAPIToggle(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = PostLikeSerializer

    def LikeView(request, pk):
        post = get_object_or_404(Post, id=request.Post.get())
        liked = False
        if post.likes.filter(id=request.user.id).exicts():
            post.likes.remove(request.user)
            liked = False
        else:
            post.likes.add(request.user)
            liked = True
