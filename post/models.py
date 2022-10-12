from random import randint

from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.text import slugify


# Create your models here.
class Post(models.Model):
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title=models.CharField(max_length=20)
    subtitle=models.CharField(blank=True,max_length=20)
    body=models.TextField()
    cover_img=models.ImageField(upload_to='static/images/%Y/%m/%d/',blank=True,null=True)
    created_date=models.DateTimeField(default=timezone.now)
    published_date=models.DateTimeField()
    slug=models.SlugField()

    class Meta:
        ordering=['created_date']

    def save(self,*args,**kwargs):
        if not self.id:
            self.slug=slugify(self.title)+'-'+str(randint(0,10**5))
        super(Post,self).save(*args,**kwargs)

    def __str__(self):
        return str(self.title)
