from lizetest.core.models import BaseModel
from lizetest.todo.models import Task
from lizetest.accounts.models import User

from django.db import models


# Create your models here.
class Comment(BaseModel):
    comment = models.TextField(verbose_name="Comentário")
    task = models.ForeignKey(Task,on_delete=models.CASCADE,verbose_name="Tarefa")
    author = models.ForeignKey(User,on_delete=models.CASCADE,blank=True)

    def __str__(self):
        return self.comment
