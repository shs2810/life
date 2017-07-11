from django.db import models
import datetime

# Create your models here.
class LifeClass(models.Model):
    month = models.IntegerField()
    year = models.IntegerField()
    sex = models.CharField(max_length=3)
    contents = models.TextField()
    tags = models.CharField(max_length=50)

    def __str__(self):
        return self.tags
