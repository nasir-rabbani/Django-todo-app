from django.contrib import admin

# Register your models here. 
from .models import TodoList

# admin.site.register(Question)
admin.site.register(TodoList)