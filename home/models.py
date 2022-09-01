from django.db import models

# Create your models here.

# TODO: Refactor this after finishing advanced course
class Post(models.Model):
    post_title = models.CharField(max_length=255, verbose_name='Title', null=True)