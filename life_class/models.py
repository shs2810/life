from django.db import models
import datetime

# Create your models here.
class LifeClass(models.Model):
    month = models.IntegerField()
    year = models.IntegerField()
    sex = models.CharField(max_length=3)
    contents = models.TextField()
    tags = models.CharField(max_length=30)

    def __str__(self):
<<<<<<< HEAD
        return self.tags
=======
        return self.tags

>>>>>>> b3f1c715a6d245aee4000af8196a30137b243d24
