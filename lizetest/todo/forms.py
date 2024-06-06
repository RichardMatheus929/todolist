# forms.py

from django import forms
from .models import Task
from lizetest.category.serializers import CategorySerializer
from lizetest.category.models import Category

class TaskForm(forms.ModelForm):
    category = CategorySerializer
    class Meta:
        model = Task
        fields = ['title', 'description', 'category']
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(TaskForm, self).__init__(*args, **kwargs)
        if user is not None:
            self.fields['category'].queryset = Category.objects.filter(author=user)