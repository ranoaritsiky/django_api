from django.db import models

# Create your models here.

class Company(models.Model):
    name=models.CharField(max_length=100)
    nif=models.CharField(max_length=100)
    stat=models.CharField(max_length=100)
    cif=models.CharField(max_length=100)
    date_created=models.DateTimeField(auto_now_add=True)
