from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from lizetest.core.models import BaseViews
from lizetest.todo.models import Task
from .models import Category
from .forms import CategoryForm

# Create your views here.
class CategoryListView(ListView,BaseViews):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categorias'

    def get_queryset(self):
        return Category.objects.filter(author=self.request.user).order_by('-created_at')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['user'] = self.request.user.username 
        return context

class CategoryCreateView(CreateView,BaseViews):
    model = Category
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('category:category_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class CategoryUpdateView(UpdateView,BaseViews):
    model = Category
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('category:category_list')

class CategoryDeleteView(DeleteView,BaseViews):
    model = Category
    template_name = 'category_confirm_delete.html'
    success_url = reverse_lazy('category:category_list')