from django.urls import path
from .views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView, AlterTask, AlterFilter

app_name = "todo"

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('alterfilter/<str:filter_user>', AlterFilter.as_view(), name='alter_filter'),
    path('altertask/completed/<int:task_id>', AlterTask.as_view(), name='task_alter'),
    path('altertask/delete/<int:task_id>', TaskDeleteView.as_view(), name='task_delete'),
    path('task/create/', TaskCreateView.as_view(), name='task_create'),
    path('task/<int:pk>/edit/', TaskUpdateView.as_view(), name='task_edit'),
]