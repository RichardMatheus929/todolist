# forms.py

from django import forms
from .models import Task
from lizetest.category.serializers import CategorySerializer

class TaskForm(forms.ModelForm):
    category = CategorySerializer
    class Meta:
        model = Task
        fields = ['title', 'description', 'category']