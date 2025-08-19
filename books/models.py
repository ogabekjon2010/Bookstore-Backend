# books/models.py
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    genre = models.CharField(max_length=100)
    description = models.TextField()
    published_date = models.DateField()
    cover_image = models.URLField()

    def __str__(self):
        return self.title
