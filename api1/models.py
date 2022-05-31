from django.db import models

# Create your models here.

class Job(models.Model):
    name=models.CharField(max_length=100)
    date_created=models.DateTimeField(auto_now=True)
    date_updated=models.DateTimeField()
    description=models.TextField()
    def __str__(self):
        return self.name