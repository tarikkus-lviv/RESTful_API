from rest_framework import generics, authentication
from django.shortcuts import get_object_or_404
from social_network.models import Post
from .serializers import PostSerializer, DetailPostSerializer
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


# not actually working
class PostLikeAPIToggle(APIView):
    def get(self, request, pk, slug=None, Format=None):
        obj = get_object_or_404(Post)
        user = User
        updated = False
        liked = False

        if user.is_authenticated:
            if user in obj.likes.all():
                liked = False
                obj.likes.remove(user)
            else:
                liked = True
                obj.likes.add(user)
            updated = True
        data = {
            'updated':updated,
            'liked':liked
        }

        return Response(data)
