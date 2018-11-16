from django.db import models

# Create your models here.
class Alarm(models.Model):
    hour = models.TimeField()
    marker = models.CharField(max_length=256)
    status = models.CharField(default='on', max_length=3, blank=True)
    url = models.CharField(max_length=500, null=True )

