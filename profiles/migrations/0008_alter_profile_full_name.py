# Generated by Django 4.1 on 2022-11-29 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_profile_address_profile_birth_date_profile_cpf_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='full_name',
            field=models.CharField(max_length=255, verbose_name='Nome Completo'),
        ),
    ]
