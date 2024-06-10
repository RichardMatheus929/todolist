from .models import Comment
from django import forms

from lizetest.todo.serializers import TaskSerializer

class CommentForm(forms.ModelForm):
    task = TaskSerializer
    class Meta:
        model = Comment
        fields = ['comment','task']