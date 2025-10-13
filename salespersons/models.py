from django.db import models

class Salesperson(models.Model):
    username = models.CharField(max_length=120, unique=True)
    name = models.CharField(max_length=120)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.username
