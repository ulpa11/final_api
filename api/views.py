from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task

# Create your views here.

def index(request):

        data=Task.objects.last()
        return render(request,"index.html",{"data":data})

@api_view(['GET'])
def apioverview(request):
    api_urls={
        'List':'/task-list/',
        'Create':'/task-create',
    }
    return Response(api_urls)

@api_view(['GET'])
def tasklist(request):
    tasks=Task.objects.all()
    serializer=TaskSerializer(tasks,many=True)
    return Response(serializer.data)
@api_view(['POST'])
def taskcreate(request):

    serializer=TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


