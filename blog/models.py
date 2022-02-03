from pyexpat import model
from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.utils.translation import gettext as _


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    post_dt = models.DateTimeField(default=timezone.now)
    post_update = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')


    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    def __str__(self):
        return self.title






class Comment(models.Model):
    name = models.CharField(max_length=100, verbose_name='name')
    email = models.EmailField(verbose_name='email')
    body = models.TextField(verbose_name='the comment')
    comment_dt = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-comment_dt',)
