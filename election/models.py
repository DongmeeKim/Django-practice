from django.db import models

# Create your models here.

class Character(models.Model):
    name = models.CharField(max_length = 15)
    gender = models.CharField(max_length = 10)
    dormitory = models.CharField(max_length = 15)
    description = models.TextField()

    def __str__(self):
        return self.name

class Poll(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    dormitory = models.CharField(max_length = 15)

    def __str__(self):
        return self.dormitory

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    character = models.ForeignKey(Character)
    votes = models.IntegerField(default=0)

