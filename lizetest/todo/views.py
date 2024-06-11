
from django.urls import reverse_lazy
from datetime import datetime
from django.shortcuts import redirect

import pytz
from django.conf import settings

from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from lizetest.core.models import BaseViews
from .models import Task
from .forms import TaskForm
from lizetest.accounts.models import User

from django.db.models import Q

from rest_framework.views import Response, APIView


class AlterFilter(APIView):
    def get(self, request, filter_user):
        user = request.user
        user_colum = ['title', 'category', 'description',
                      'created_at', 'completion_date']

        if filter_user in user_colum:
            if user.filtro not in user_colum:
                user.filtro = 'created_at'
                user.save()
                return Response({'Filtro_atualizado': 'created_at'})
            else:
                user.filtro = filter_user
                user.save()
                return Response({'filtro_atualizado': filter_user})


class AlterTask(APIView):
    def get(self, rquest, task_id):
        task = Task.objects.get(id=task_id)
        task.completed = not task.completed
        if task.completion_date:
            task.completion_date = None
        else:
            local_tz = pytz.timezone(settings.TIME_ZONE)
            now = datetime.now(local_tz)
            task.completion_date = now
        task.save()
        return Response({'id_atualizado': task_id, "valor": task.completed})


class TaskListView(ListView, BaseViews):
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
        context['user'] = self.request.user.username

        filtro_select = {
            "title": "por nome",
            "description":"por descrição",
            "category":"por categoria",
            "created_at":"por data de criação",
            "completion_date": "por task completa",
        }

        context['filtro'] = filtro_select[self.request.user.filtro]

        query = self.request.GET.get('query_task')

        if query:
            context['teste'] = Task.objects.filter(author=self.request.user.id).filter(
                Q(title__icontains=query) |
                Q(category__name__icontains=query)
            )
            context['filtro'] = "pesquisa"
            return context

        if self.request.user.filtro == "created_at":
            context['teste'] = Task.objects.filter(
                author=self.request.user.id).all().order_by('-created_at')
            return context
        else:
            context['teste'] = Task.objects.filter(
                author=self.request.user.id).all().order_by(self.request.user.filtro)
            return context


class TaskCreateView(CreateView, BaseViews):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('todo:task_list')

    def get_form_kwargs(self):
        kwargs = super(TaskCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskUpdateView(UpdateView, BaseViews):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('todo:task_list')


class TaskDeleteView(APIView):
    def get(self, request, task_id):
        try:
            task = Task.objects.get(id=task_id)
            if task.completed:
                return Response({'sucess': False})
            else:
                task.delete()
                return Response({'sucess': True})
        except:
            return Response({'sucess': False})

    # def delete(self, request, *args, **kwargs):
    #     from django.http import HttpResponseRedirect
    #     self.object = self.get_object()
    #     task_status = self.object.completed

    #     if task_status:
    #         success_url = reverse_lazy('todo:endpoint_task_delete')
    #     else:
    #         success_url = self.get_success_url()
    #         self.object.delete()
    #         return HttpResponseRedirect(success_url)
