from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название жанра')

    def __str__(self):
        return self.name