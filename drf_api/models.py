from django.contrib.auth.models import User
from django.db import models
from slug import slug


# Create your models here.

class Singer(models.Model):
    name = models.CharField(max_length=255, verbose_name='Исполнитель', unique=True)
    slug = models.SlugField(max_length=255, db_index=True, verbose_name='Слаг', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author', verbose_name='автор')

    def save(self, *args, **kwargs):
        self.slug = slug(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'


class Album(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    singer = models.ForeignKey(Singer, related_name='singer', on_delete=models.CASCADE, verbose_name="Исполнитель")
    year_published = models.PositiveSmallIntegerField(verbose_name='Год выпуска')
    slug = models.SlugField(max_length=255, db_index=True, verbose_name='Слаг', blank=True)

    def save(self, *args, **kwargs):
        self.slug = slug(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'


class Song(models.Model):
    title = models.CharField(max_length=255, verbose_name='Песня')
    album = models.ForeignKey(Album, on_delete=models.CASCADE, verbose_name='Альбом', )
    slug = models.SlugField(max_length=255, db_index=True, verbose_name='Слаг', blank=True)

    def save(self, *args, **kwargs):
        self.slug = slug(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Песня'
        verbose_name_plural = 'Песни'
