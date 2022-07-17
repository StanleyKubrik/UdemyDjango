from django.db import models


# Create your models here.
class Order(models.Model):
    order_dt = models.DateTimeField(auto_now=True)
    order_name = models.CharField(max_length=200, verbose_name='Имя')
    order_phone = models.CharField(max_length=200, verbose_name='Телефон')

    def __str__(self):
        return f'{self.id} - {self.order_name}'

    class Meta:
        verbose_name = 'Замовлення'
        verbose_name_plural = 'Замовлення'
