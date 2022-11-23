from django.db import models
from datetime import datetime


# TODO: Refactor this after finishing advanced course
class Post(models.Model):
    post_title = models.CharField(
            max_length=255, 
            verbose_name='Title',
            default='default_title'
        )
    post_text = models.TextField(
            verbose_name='Text',
            default='default_text'
        )
    post_img = models.ImageField(
            verbose_name='Img', 
            upload_to='blog/posts/%d/%m/%Y',
            null=True
        )
    post_date = models.DateTimeField(
            verbose_name='Data', 
            auto_now_add=datetime.now,
            null=True
        )
    post_author = models.CharField(
            max_length=255, 
            verbose_name='Autor',
            default='default_author'
        )