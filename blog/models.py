import email
from email.policy import default
import profile
from time import time
from django.conf import settings
from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager

# Create your models here.
class Author(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email=models.EmailField()
    registered_at=models.DateTimeField(default=timezone.now)
    last_login=models.DateTimeField(blank=True,null=True)
    profile=models.TextField()
    profile_photo=models.ImageField(upload_to='static/images/users/')

    def __str__(self):
        return self.first_name +" "+ self.last_name

class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    # time_to_read=models.IntegerField(blank=True,null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    image=models.ImageField(upload_to='static/images/%Y/%m/%d/')
    tags=TaggableManager()


    def publish(self):
        self.published_date = timezone.now()
        # self.time_to_read = len(self.text)//200
        self.save()

    def __str__(self):
        return self.title



class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text