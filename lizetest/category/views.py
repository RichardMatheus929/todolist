from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from lizetest.core.models import BaseViews
from .models import Category
from .forms import CategoryForm

# Create your views here.
class CategoryListView(ListView,BaseViews):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categorias'

class CategoryCreateView(CreateView,BaseViews):
    model = Category
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('category:category_list')

class CategoryUpdateView(UpdateView,BaseViews):
    model = Category
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('category:category_list')

class CategoryDeleteView(DeleteView,BaseViews):
    model = Category
    template_name = 'category_confirm_delete.html'
    success_url = reverse_lazy('category:category_list')