from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=120)
    notes = models.TextField(blank=True)

    def __str__(self):
        return str(self.name)
