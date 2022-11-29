# Generated by Django 4.1 on 2022-11-29 01:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.constraints
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0003_profile_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=django.db.models.constraints.UniqueConstraint, verbose_name='Email'),
        ),
    ]
