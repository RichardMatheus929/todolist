from django.db import models
from lizetest.core.models import BaseModel

from lizetest.accounts.models import User

class Category(BaseModel):
    name = models.CharField(max_length=255)
    author = models.ForeignKey(User,on_delete=models.CASCADE,blank=True)

    def __str__(self):
        return self.name