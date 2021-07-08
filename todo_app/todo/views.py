from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView

from .models import Task


class TaskList(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'


class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    template_name = 'task_form.html'
    success_url = reverse_lazy('tasks')


class TaskDetail(DetailView):
    model = Task
    template_name = 'task_detail.html'
    context_object_name = 'task'


class TaskEdit(UpdateView):
    model = Task
    fields = '__all__'
    template_name = 'task_form.html'
    success_url = reverse_lazy('tasks')
