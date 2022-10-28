from django.conf import settings
from django.db import models

from post.models import Post


# Create your models here.
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    published_at = models.DateTimeField()

    class Meta:
        ordering = ['published_at']

    def __str__(self):
        return str(self.id)
