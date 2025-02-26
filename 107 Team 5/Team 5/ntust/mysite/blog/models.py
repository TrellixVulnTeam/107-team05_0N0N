
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone


class Post(models.Model):
    p_id = models.AutoField(primary_key = True)
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return  str(self.p_id) + "." + self.title

class Comment(models.Model):
    title = models.CharField(max_length =200)
    user_name = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    pub_date = models.DateTimeField(default=timezone.now)
    post = models.IntegerField(default=0)

    def __str__(self):
        return self.title




