from django.db import models

class Movie(models.Model):
    STATUS_CHOICES = [
        ('watched', 'Watched'),
        ('to_watch', 'To Watch')
    ]
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    release_year = models.IntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='to_watch')

    def __str__(self):
        return self.title

