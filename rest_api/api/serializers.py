from rest_framework import serializers

from social_network.models import Post, likes


class PostSerializer(serializers.ModelSerializer):
    # likes = serializers.IntegerField(max_value=50)
    # dislikes = serializers.IntegerField(max_value=50)

    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'body', 'like', 'likes', 'dislikes')

class DetailPostSerializer(serializers.ModelSerializer):
    # likes = serializers.IntegerField(max_value=50)
    # dislikes = serializers.IntegerField(max_value=50)

    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'body', 'like', 'likes', 'dislikes')

# class LikesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = likes
#         fields = '__all__'
