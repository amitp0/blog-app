from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.conf import settings
# Create your models here.
class Post(models.Model):
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title=models.CharField(max_length=20)
    subtitle=models.CharField(blank=True,max_length=20)
    body=models.TextField()
    cover_img=models.ImageField(upload_to='static/images/%Y/%m/%d/',blank=True)
    created_date=models.DateTimeField(default=timezone.now)
    published_date=models.DateTimeField()
    slug=models.SlugField()

    class Meta:
        ordering=['created_date']

    def save(self,*args,**kwargs):
        if not self.id:
            self.slug=slugify(self.title)
        super(Post,self).save(*args,**kwargs)

    def __str__(self):
        return str(self.title)