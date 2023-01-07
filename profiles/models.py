from django.db import models
from django.contrib.auth.models import User


#TODO: Add profession to profile
#TODO: Profile should create without email

class Profile(models.Model):

    def __str__(self):
        return self.full_name

    email = models.OneToOneField(
        User,
        null=True, 
        unique=True,
        verbose_name='Email', 
        on_delete=models.CASCADE
    )
    full_name = models.CharField(
        max_length=255, 
        verbose_name='Nome Completo',
    )
    birth_date = models.DateField(
        verbose_name='Data de nascimento', 
        null=True
    )
    cpf = models.CharField(
        verbose_name='CPF',
        max_length=255,
        null=True
    )
    rg = models.CharField(
        verbose_name='RG',
        max_length=255,
        null=True
    )
    address = models.CharField(
        verbose_name='Endereço',
        max_length=255,
        null=True
    )
    phone_1 = models.CharField(
        verbose_name='Contato',
        max_length=255,
        null=True
    )
    phone_2 = models.CharField(
        verbose_name='Contato 2',
        max_length=255,
        null=True
    )