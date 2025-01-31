from django.urls import path
from django.contrib.auth import views as auth_views

from .views import SignUpView,LoginView


app_name="accounts"

urlpatterns = [
    path('singup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('singout/', auth_views.LogoutView.as_view(next_page='accounts:login'), name='logout'),
]