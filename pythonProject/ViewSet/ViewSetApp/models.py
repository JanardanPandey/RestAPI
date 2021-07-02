from django.db import models

# Create your models here.
class ITAssetsModel(models.Model):
    region = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    svc = models.CharField(max_length=10)
    assetsname = models.CharField(max_length=100)