from django.shortcuts import render
from django.http import HttpResponse
from .models import TodoList
from django.utils import timezone

# Create your views here.

def getTodos():
    all_todos = TodoList.objects.all()
    return {'todos': all_todos}
    
def home(request):
    return render(request, "index.html")
    
def todo(request):
    return render(request, "todo.html", getTodos())

def save_todo(request):
    """
    docstring
    """
    print("save_todo called")
    name = request.POST['name']
    date = request.POST['date']
    created_on = timezone.now()

    todo = TodoList(name=name, date=date, created_on=created_on)
    todo.save()

    return render(request, "todo.html", getTodos())

