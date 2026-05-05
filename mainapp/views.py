from django.shortcuts import render

from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets, pagination
from .serializers import Application_Serializer, Category_Serializer, Worker_Serializer
from .models import Application, Worker, Category
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

""" Pagionation class """

class our_pagination(pagination.PageNumberPagination):
    """  """
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 10000

class our_pagination1(pagination.PageNumberPagination):
    """  """
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 10000

    """ Throttling """

from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
class User_throttle(AnonRateThrottle):
    scope = 'example'

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = Application_Serializer
    pagination_class = our_pagination1
    throttle_classes = [User_throttle,]

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    # filterset_fields = ['category', 'applicant']  
    
    search_fields = ['name', 'body']
    ordering_fields = ['created_at']

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.filter(status=True)
    serializer_class = Category_Serializer

class WorkerViewSet(viewsets.ModelViewSet):
    queryset = Worker.objects.filter(status=True)
    serializer_class = Worker_Serializer
    pagination_class = our_pagination
    throttle_classes = [User_throttle,]

