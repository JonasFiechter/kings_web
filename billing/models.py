from django.db import models
from django.contrib.auth.models import User
from profiles.models import Profile


class Contract(models.Model):
    created_at = models.DateField(
        verbose_name='Data de criação', 
        auto_now_add=True
    )
    owner = models.ForeignKey(
        User,
        verbose_name='Titular do contrato',
        on_delete=models.DO_NOTHING
    )
    value = models.FloatField(
        verbose_name='Valor',
    )
    registration_fee = models.FloatField(
        verbose_name='Matrícula',
    )
    registration_fee_status = models.BooleanField(
        verbose_name='Status Matrícula'
    )
    reference_year = models.IntegerField(
        verbose_name='Ano de referência',
    )
    student = models.ForeignKey(
        Profile,
        verbose_name='Aluno',
        on_delete=models.DO_NOTHING
    )
    comments = models.TextField(
        verbose_name='Comentários',
        max_length=1000
    )
    status = models.BooleanField(
        verbose_name='Status do contrato'
    )
    tuition_jan = models.BooleanField(
        verbose_name='Janeiro',
    )
    tuition_feb = models.BooleanField(
        verbose_name='Fevereiro',
    )
    tuition_mar = models.BooleanField(
        verbose_name='Março',
    )
    tuition_apr = models.BooleanField(
        verbose_name='Abril',
    )
    tuition_may = models.BooleanField(
        verbose_name='Maio',
    )
    tuition_jun = models.BooleanField(
        verbose_name='Junho',
    )
    tuition_jul = models.BooleanField(
        verbose_name='Julho',
    )
    tuition_aug = models.BooleanField(
        verbose_name='Agosto',
    )
    tuition_set = models.BooleanField(
        verbose_name='Setembro',
    )
    tuition_oct = models.BooleanField(
        verbose_name='Outubro',
    )
    tuition_nov = models.BooleanField(
        verbose_name='Novembro',
    )
    tuition_dec = models.BooleanField(
        verbose_name='Dezembro',
    )