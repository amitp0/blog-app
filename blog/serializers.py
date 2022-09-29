from rest_framework import serializers
from .models import Author,Post
from django.utils import timezone


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields='__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields='__all__'