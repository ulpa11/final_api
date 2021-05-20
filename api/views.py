from django.shortcuts import render
from django.http import  HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Data,Client
from .serializers import DataSerializer,ClientSerializer
#impleanting djnago token authentication system
from rest_framework.permissions import IsAuthenticated


# Create your views here.
def index(request):
    index_data=Client.objects.last()
    return render(request,"index.html",{"data":index_data})

def tables(request):
    index_data=Client.objects.all()
    return render(request,"tables.html",{"data":index_data})



class ClientViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ClientSerializer
    def get_queryset(self):
        client = Client.objects.all()
        return client
    def create(self,request,*args,**kwargs):
        sensor_data=request.data
        new_data=Data.objects.create(d1=sensor_data["data"]["d1"],d2=sensor_data["data"]["d2"])
        new_data.save()

        new_client_data=Client.objects.create(client_name=sensor_data["client_name"],device_name=sensor_data["device_name"],data=new_data)
        new_client_data.save()

        serializer=ClientSerializer(new_client_data)
        return Response(serializer.data)

class DataViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = DataSerializer
    def get_queryset(self):
        data= Data.objects.all()
        return data