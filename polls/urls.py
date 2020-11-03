from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('todo', views.todo, name='todo'),
    path('save_todo', views.save_todo, name='save_todo'),
]
