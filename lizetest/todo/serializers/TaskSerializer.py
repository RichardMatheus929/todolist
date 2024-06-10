from rest_framework.serializers import ModelSerializer
from lizetest.todo.models import Task

class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ('title')