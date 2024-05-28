from django.db import models


# Create your models here.

class Poem(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.CharField(max_length=255, verbose_name="Автор")
    title = models.CharField(max_length=255, verbose_name='Название')
    lyrics = models.TextField(verbose_name="Текст")
