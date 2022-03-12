from django.db import models
from django.core.validators import MinValueValidator



class Category(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name='Название' )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.name}'


class News(models.Model):
    User = models.CharField(max_length=20, verbose_name='Автор')
    name = models.CharField(max_length=20,unique=True, verbose_name='Название!')
    description = models.TextField(max_length=180, verbose_name='Описание')
    quantity = models.IntegerField(
        validators=[MinValueValidator(0, 'Quantity should be >= 0')], verbose_name='Количество')
    price = models.FloatField(default=0.0, verbose_name='Цена')
    category = models.ForeignKey('Category', max_length=15, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Категория')
    date_pub = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')


    class Meta:
        verbose_name = 'Разновидность'
        verbose_name_plural = 'Разновидности'


    def __str__(self):
        return f'{self.name}{self.quantity}'

    def get_absolute_url(self):
        return f'/News/{self.id}'




