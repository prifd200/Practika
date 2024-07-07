from django.db import models


class gorod(models.Model):
    City = models.CharField(max_length=30, verbose_name='Город')

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return self.City
class ulica(models.Model):
    Street = models.CharField(max_length=30, verbose_name='Улица')
    City = models.CharField(max_length=30, verbose_name='Город')
    id_City = models.ForeignKey(gorod, on_delete= models.CASCADE)
    class Meta:
        verbose_name = 'Улица'
        verbose_name_plural = 'Улицы'

    def __str__(self):
        return self.Street
class magaz(models.Model):
    Shop = models.CharField(max_length=30, verbose_name='Магазин')
    City = models.CharField(max_length=30, verbose_name='Город')
    Street = models.CharField(max_length=30, verbose_name='Улица')
    Building = models.CharField(max_length=30, verbose_name='Дом')
    Open = models.TimeField(verbose_name='Время открытия',auto_now=False, auto_now_add=False)
    Close = models.TimeField(verbose_name='Время закрытия',auto_now=False, auto_now_add=False)
    id_City = models.ForeignKey(gorod, on_delete=models.CASCADE)
    id_Street = models.ForeignKey(ulica, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'

    def __str__(self):
        return self.Shop
# Create your models here.
