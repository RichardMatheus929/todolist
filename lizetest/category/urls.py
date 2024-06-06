from django.urls import path

from .views import CategoryListView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView

app_name = "category"

urlpatterns = [

    path('', CategoryListView.as_view(), name='category_list'),
    path('create/', CategoryCreateView.as_view(), name='category_create'),
    path('edit<int:pk>/', CategoryUpdateView.as_view(), name='category_edit'),
    path('delete<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),
]