from django.urls import path

from .views import CategoryListView, CategoryCreateView, CategoryUpdateView

app_name = "category"

urlpatterns = [

    path('list/', CategoryListView.as_view(), name='category_list'),
    path('create/', CategoryCreateView.as_view(), name='category_create'),
    path('update/', CategoryUpdateView.as_view(), name='category_update'),
]