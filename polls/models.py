import datetime

from django.db import models
from django.utils import timezone

class TodoList(models.Model):
    """
    To store Todo list
    """
    name = models.CharField('Todo Name', max_length=500)
    date = models.CharField(max_length=10)
    created_on = models.DateTimeField()

    def __str__ (self):
        return self.name
