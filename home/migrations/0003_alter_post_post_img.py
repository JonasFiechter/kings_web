# Generated by Django 4.1 on 2022-11-23 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_post_post_author_post_post_date_post_post_img_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_img',
            field=models.ImageField(null=True, upload_to='blog/posts/%d/%m/%Y/', verbose_name='Img'),
        ),
    ]