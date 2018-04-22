from django.db import models

# Create your models here.

class Character(models.Model):
    name = models.CharField(max_length = 15)
    gender = models.CharField(max_length = 10)
    dormitory = models.CharField(max_length = 15)
    description = models.TextField()

    def __str__(self):
        return self.name