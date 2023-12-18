from django.db import models


class Prod(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя товара')
    price = models.IntegerField()
    count = models.IntegerField()
    description = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}, {self.price}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
