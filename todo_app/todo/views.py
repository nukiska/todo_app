from django import http
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView

from .models import Task
from .widgets import DatePickerWidget


class HomePageView(TemplateView):
    template_name = 'index.html'


class AppGalleryView(TemplateView):
    template_name = 'todo/app_gallery.html'


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(completed=False).count()

        search_task = self.request.GET.get('searchbar') or ''
        if search_task:
            context['tasks'] = context['tasks'].filter(title__icontains=search_task)
        context['search_task'] = search_task
        return context


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'completed', 'deadline']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)

    def get_form(self):
        form = super(TaskCreate, self).get_form()
        form.fields['deadline'].widget = DatePickerWidget()
        return form


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'

    def get_object(self):
        task = super(TaskDetail, self).get_object()
        if task.user != self.request.user:
            raise http.Http404
        return task


class TaskEdit(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'completed', 'deadline']
    success_url = reverse_lazy('tasks')

    def get_object(self):
        task = super(TaskEdit, self).get_object()
        if task.user != self.request.user:
            raise http.Http404
        return task

    def get_form(self):
        form = super(TaskEdit, self).get_form()
        form.fields['deadline'].widget = DatePickerWidget()
        return form


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('tasks')

    def get_object(self):
        task = super(TaskDelete, self).get_object()
        if task.user != self.request.user:
            raise http.Http404
        return task
