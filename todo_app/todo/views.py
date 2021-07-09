from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from .models import Task


class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'


class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')


class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'


class TaskEdit(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')


class TaskDelete(DeleteView):
    model = Task
    success_url = reverse_lazy('tasks')
