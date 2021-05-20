from django.db import models

# Create your models here.
class Data(models.Model):
    d1 = models.IntegerField(default=0)
    d2 = models.IntegerField(default=0)

class Client(models.Model):
    client_name=models.CharField(max_length=200)
    device_name=models.CharField(max_length=200)
    data=models.OneToOneField(Data,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.client_name