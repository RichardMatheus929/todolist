# models.py
from django.db import models
from django.conf import settings

from lizetest.core.models import BaseModel
from lizetest.category.models import Category
from lizetest.accounts.models import User

class Task(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    completion_date = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    author = models.ForeignKey(User,on_delete=models.CASCADE,blank=True)

    def __str__(self):
        return self.title