from django.db import models

# Create your models here.
class Alarm(models.Model):
    hour = models.TimeField()
    marker = models.CharField(max_length=256)
