from rest_framework import serializers
from .models import Post, Tag
from django.contrib.auth.models import User


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')
        # exclude = ('password')


class PostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'slug', 'text', 'is_publish', 'user', 'tags')
