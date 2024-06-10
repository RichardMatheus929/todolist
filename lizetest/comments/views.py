from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Comment
from .forms import CommentForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from lizetest.core.models import BaseViews


# Create your views here.
class CommentsListView(ListView,BaseViews):
    model = Comment
    template_name = 'comments_list.html'
    context_object_name = 'comments'

    def get_queryset(self):
        return Comment.objects.filter(author=self.request.user)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user.username
        return context
    
class CommentsCreateView(CreateView,BaseViews):
    model = Comment
    form_class = CommentForm
    template_name = 'comment_form.html'
    success_url = reverse_lazy('comments:comments_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class CommentsEditView(UpdateView,BaseViews):
    model = Comment
    form_class = CommentForm
    template_name = 'comment_form.html'
    success_url = reverse_lazy('comments:comments_list')

class CommentDeleteView(DeleteView,BaseViews):
    model = Comment
    template_name = 'comments_confirm_delete.html'
    success_url = reverse_lazy('comments:comments_list')