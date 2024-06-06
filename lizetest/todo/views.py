
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from lizetest.core.models import BaseViews
from .models import Task
from .forms import TaskForm
from lizetest.accounts.models import User

from django.db.models import Q

class TaskListView(ListView,BaseViews):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        queryset = Task.objects.filter(author=self.request.user)
        query = self.request.GET.get('query_task')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(category__name__icontains=query)
            )
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['number_tasks'] = self.get_queryset().count()
        return context

class TaskCreateView(CreateView,BaseViews):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('todo:task_list')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class TaskUpdateView(UpdateView,BaseViews):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('todo:task_list')



class TaskDeleteView(DeleteView,BaseViews):
    model = Task
    template_name = 'task_confirm_delete.html'
    success_url = reverse_lazy('todo:task_list')

