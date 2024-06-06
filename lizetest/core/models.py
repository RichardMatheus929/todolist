from django.shortcuts import redirect
from django.db import models
from django.views import View



class BaseModel(models.Model):
	created_at  = models.DateTimeField(verbose_name='Registrado em', auto_now_add=True, db_index=True)
	updated_at = models.DateTimeField(verbose_name='Atualizado em', auto_now=True)

	class Meta:
		abstract = True
          
class BaseViews(View):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        return super().dispatch(request, *args, **kwargs)
    
    def get_queryset(self):
        from lizetest.todo.models import Task
        # Obtém o usuário atual
        user = self.request.user
        # Filtra as tarefas pelo autor
        return Task.objects.filter(author=user)
