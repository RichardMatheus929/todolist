from django.urls import path

from .views import CommentsListView,CommentsCreateView,CommentsEditView,CommentDeleteView

app_name = "comments"

urlpatterns = [

    path('', CommentsListView.as_view(), name='comments_list'),
    path('create/', CommentsCreateView.as_view(), name='comments_create'),
    path('edit<int:pk>/', CommentsEditView.as_view(), name='comments_edit'),
    path('delete<int:pk>/', CommentDeleteView.as_view(), name='comments_delete'),
]