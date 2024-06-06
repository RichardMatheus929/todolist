
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Task
from .forms import TaskForm
from lizetest.accounts.models import User

class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:  # Sua condição aqui
            return redirect('accounts:login')
        return super().dispatch(request, *args, **kwargs)


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('todo:task_list')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:  # Sua condição aqui
            return redirect('accounts:login')
        return super().dispatch(request, *args, **kwargs)


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('todo:task_list')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:  # Sua condição aqui
            return redirect('accounts:login')
        return super().dispatch(request, *args, **kwargs)


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_confirm_delete.html'
    success_url = reverse_lazy('todo:task_list')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:  # Sua condição aqui
            return redirect('accounts:login')
        return super().dispatch(request, *args, **kwargs)
