from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name='Название')
    author = models.ForeignKey('Author', on_delete=models.CASCADE, verbose_name='Автор')
    description = models.TextField(max_length=300, null=False, blank=False, verbose_name='Описание')
    image = models.ImageField(upload_to='photos', null=False, blank=False, verbose_name='Изображения')
    article = models.CharField(max_length=6, unique=True, verbose_name='Артикл')
    genres = models.ManyToManyField('Genre', verbose_name='Жанры')
    publication_date = models.DateField(verbose_name='Дата публикации')
    price = models.PositiveIntegerField(default=0, verbose_name='Цена')
    is_available = models.BooleanField(default=True, verbose_name='В наличии')
    language = models.ManyToManyField('Language', verbose_name='Языки')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return self.title