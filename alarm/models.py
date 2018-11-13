from django.db import models

# Create your models here.
class Alarm(models.Model):
    hour = models.DateTimeField()
    marker = models.CharField(max_length=256)
