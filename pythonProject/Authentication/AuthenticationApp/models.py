from django.db import models

# Create your models here.
class ItAssets(models.Model):
    city = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    svc = models.CharField(max_length=100)
    branch_code = models.IntegerField()