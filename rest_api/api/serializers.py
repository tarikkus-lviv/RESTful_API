from rest_framework import serializers

from social_network.models import Post, Like


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'body', 'post_date', 'likes')

class DetailPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'body', 'post_date', 'likes')

class PostLikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = ('id', 'user', 'post', 'value')
