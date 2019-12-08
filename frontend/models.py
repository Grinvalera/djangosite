from django.db import models
from django.core.exceptions import ValidationError


class Subscribers(models.Model):
    email = models.CharField(max_length=50, verbose_name='Email', unique=True)
    name = models.CharField(max_length=128)
    # phone_number = models.CharField(max_length=20, null=True)

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'Подписчик'
        verbose_name_plural = 'Подписчики'
