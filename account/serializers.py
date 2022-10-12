from rest_framework import serializers
from .models import User

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','first_name','last_name','profile_photo','about']