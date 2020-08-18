from rest_framework import generics
from social_network.models import Post
from .serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly

class PostAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class DetailPostAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# login(request, user)
# LogTime.objects.create(user=request.user)
