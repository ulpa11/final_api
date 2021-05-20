from rest_framework import serializers
from .models import Data,Client



class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Client
        fields=["id","client_name", "device_name","data"]
        depth=1

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model=Data
        fields=["id","d1", "d2"]
