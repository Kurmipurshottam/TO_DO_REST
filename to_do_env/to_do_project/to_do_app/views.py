from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import Taskserializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def task_list(request):
    task=Task.objects.all()
    serializer=Taskserializers(task,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_task(request):
    serializer = Taskserializers(data=request.data)  
    if serializer.is_valid():  
        serializer.save()  
        return Response(serializer.data, status=201) 
    return Response(serializer.errors, status=400)

@api_view(['PUT', 'PATCH'])
def update_task(request, pk):  
    try:
        task = Task.objects.get(pk=pk)  
    except Task.DoesNotExist:  
        return Response(status=404)  
    
    serializer = Taskserializers(task, data=request.data, partial=True)  
    if serializer.is_valid():  
        serializer.save()  
        return Response(serializer.data) 
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_task(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:  
        return Response(status=404) 
    
    task.delete() 
    return Response(status=204)




