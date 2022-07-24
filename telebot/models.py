from django.db import models


# Create your models here.
class TeleSettings(models.Model):
    tg_token = models.CharField(max_length=200, verbose_name='Токен')
    tg_chat_id = models.CharField(max_length=200, verbose_name='Чат ID')
    tg_message = models.TextField(verbose_name='Сообщение')

    def __str__(self):
        return self.tg_chat_id

    class Meta:
        verbose_name = 'Настройку'
        verbose_name_plural = 'Настройки'
