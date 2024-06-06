from django.urls import reverse_lazy
from django.contrib.auth import login
from django.views.generic import FormView

from .forms import CustomUserCreationForm

from django.contrib.auth import views as auth_views


class SignUpView(FormView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('accounts:login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class LoginView(auth_views.LoginView):
    def get_success_url(self):
        return reverse_lazy('todo:task_list')
