from django.db import models
from django.core.exceptions import ValidationError

from products.models import Product


class Status(models.Model):
    name = models.CharField(max_length=24, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    create = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return f'status: {self.name}'

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Order(models.Model):
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    comment = models.TextField(blank=True, null=True, default=None)
    customer_email = models.CharField(max_length=50, verbose_name='Email', unique=True)
    customer_name = models.CharField(max_length=128)
    customer_phone = models.CharField(max_length=20, blank=True, null=True, default=None)
    create = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return f'{self.customer_name}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, blank=True, null=True, default=None, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    create = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now_add=False, auto_now=True)
    # customer_email = models.CharField(max_length=50, verbose_name='Email', unique=True)
    # customer_name = models.CharField(max_length=128)
    # customer_phone = models.CharField(max_length=20, blank=True, null=True, default=None)

    def __str__(self):
        return f'orders{self.id, self.status.name}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
