from rest_framework import serializers
from .models import account

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model=account
        fields='__all__'