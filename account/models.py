from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    about=models.TextField()
    profile_photo=models.ImageField(upload_to='static/images/users/')

    def __str__(self):
        return str(self.username)
        