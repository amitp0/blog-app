from rest_framework import serializers
from .models import Author
from django.utils import timezone


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields=["user","first_name","last_name","email","registered_at","last_login","profile","profile_photo"]


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields=["user","first_name","last_name","email","registered_at","last_login","profile","profile_photo"]
