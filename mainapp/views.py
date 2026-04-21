from django.shortcuts import render

from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets, pagination
from .serializers import Application_Serializer, Category_Serializer, Worker_Serializer
from .models import Application, Worker, Category
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from rest_framework.views import APIView

class ExampleView(APIView):
    throttle_classes = [UserRateThrottle]

    def get(self, request, format=None):
        content = {
            'status': 'request was permitted'
        }
        return Response(content)


""" Pagionation class """
class our_pagination(pagination.PageNumberPagination):
    """  """
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 10000

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = Application_Serializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.filter(status=True)
    serializer_class = Category_Serializer

class WorkerViewSet(viewsets.ModelViewSet):
    queryset = Worker.objects.filter(status=True)
    serializer_class = Worker_Serializer
    pagination_class = our_pagination
