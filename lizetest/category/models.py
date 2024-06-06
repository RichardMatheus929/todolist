from django.db import models
from lizetest.core.models import BaseModel

class Category(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name