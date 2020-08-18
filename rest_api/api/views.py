from rest_framework import generics
from social_network.models import Post, likes
from .serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly

from django.db.models import Count, Sum, Value
from django.db.models.functions import Coalesce

class PostAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class DetailPostAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    # queryset = Post.objects.all()
    queryset = likes.objects.annotate(
        likes = Coalesce(Sum('likes__isLike'), Value(0)),
        dislike = Coalesce(Count('likes')-Sum('likes__isLike'), Value(0))
    )
    serializer_class = DetailPostSerializer

class LikesViewSet(viewsets.ModelViewSet):
    queryset = likes.objects.all()
    permission_classes = [
        permissions.AllowAny
        # permissions.IsAuthenticated,
    ]
    serializer_class = LikesSerializer




# login(request, user)
# LogTime.objects.create(user=request.user)
