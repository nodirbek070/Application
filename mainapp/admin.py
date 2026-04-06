from django.contrib import admin
from  .models import Category, Application, Worker


# Register your models here.



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', "status")
    list_filter = ('status', )

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', "category", "applicant", "phone1", "status")
    list_filter = ('status', "category", "created_on")
    search_fields = ('name', 'body', 'phone1', "phone2")
    list_per_page = 5

@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('full_name', "stage", "phone1", "status")
    list_filter = ('status', )




