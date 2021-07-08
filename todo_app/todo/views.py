from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Task


class TaskList(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'


class TaskDetail(DetailView):
    model = Task
    template_name = 'task_detail.html'
    context_object_name = 'task'
