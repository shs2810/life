from django.db import models
from django.utils import timezone

import datetime

# Create your models here.
class LifeClass(models.Model):
    year = models.IntegerField()
    month = models.IntegerField()
    sex = models.CharField(max_length=5)
    contents = models.TextField()
    tags = models.CharField(max_length=30)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.tags

class Comment(models.Model):
    pass
   # lifeclass = models.ForeignKey(LifeClass) #LifeClass 글이랑 댓글 1:1 관계

