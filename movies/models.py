from django.db import models

class Movie(models.Model):
    REGION_CHOICES = [
        ('Asia', '日韩'),
        ('Europe', '欧美'),
        ('China', '中国'),
    ]

    title = models.CharField(max_length=100)
    release_year = models.IntegerField()
    genre = models.CharField(max_length=50)
    description = models.TextField()
    poster = models.ImageField(upload_to='posters/')
    region = models.CharField(max_length=10, choices=REGION_CHOICES, default='Asia')

    def __str__(self):
        return self.title
