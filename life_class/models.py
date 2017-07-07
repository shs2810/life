from django.db import models
import datetime

# Create your models here.
class LifeClass(models.Model):
    month = models.IntegerField()
    year = models.IntegerField()
    sex = models.CharField(max_length=10)
    title = models.CharField(max_length=200)
    contents = models.TextField()

    def __str__(self):
        return self.title
