from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=30, verbose_name='Язык')

    def __str__(self):
        return self.name