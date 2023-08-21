from django.db import models
from django.utils.translation import gettext_lazy as _


class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField()

    def __str__(self):
        return self.name


class Documentation(models.Model):
    TYPE_CHOICES = (
        ('B', _('Book')),
        ('A', _('Article')),
    )
    STATUS_CHOICES = (
        ('A', _('Available')),
        ('U', _('Unavailable')),
    )

    name = models.CharField(max_length=250)
    type = models.CharField(max_length=1, choices=TYPE_CHOICES, default='B')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='A')
    price = models.FloatField()
    description = models.TextField()
    author = models.ForeignKey(to=Author, on_delete=models.CASCADE, related_name='author')
    city = models.ForeignKey(to=City, on_delete=models.CASCADE, related_name='city')
    genre = models.ForeignKey(to=Genre, on_delete=models.CASCADE, related_name='genre')

    def __str__(self):
        return str(self.name)
