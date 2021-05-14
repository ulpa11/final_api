from django.db import models

# Create your models here.
class Task(models.Model):
    API_Key=models.CharField(max_length=200)
    mac=models.CharField(max_length=200)
    field=models.IntegerField()
    data=models.IntegerField()

    def __str__(self):
        return self.API_Key

