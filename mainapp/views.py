from django.shortcuts import render

from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from .serializers import Application_Serializer, Category_Serializer, Worker_Serializer
from .models import Application, Worker, Category

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.filter(status='qabul_qilingan')
    serializer_class = Application_Serializer
    
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.filter(status=True)
    serializer_class = Category_Serializer

class WorkerViewSet(viewsets.ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = Worker_Serializer
