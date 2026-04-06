from rest_framework import  serializers
from .models import Application, Worker, Category


class Application_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ["id", "name", "category", "body", 'photo', 'video', 'applicant', 'phone1', 'phone2', 'status', 'created_on']
        
class Category_Serializer(serializers.ModelSerializer):
    applications = Application_Serializer(many=True, read_only = True)
    class Meta:
        model = Category
        fields = ['id', 'name', 'status', 'applications']
        
class Worker_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = ['id', 'full_name', 'status', 'photo', 'stage', 'phone1', 'phone2']
        
        
    



