from django.db import models

# Create your models here.
class Alarm(models.Model):
    hour = models.TimeField()
    marker = models.CharField(max_length=256)
    status = models.BooleanField(default=True)
    url = models.CharField(max_length=500, null=True )

