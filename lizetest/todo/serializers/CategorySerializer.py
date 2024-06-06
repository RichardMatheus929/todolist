from rest_framework.serializers import ModelSerializer
from lizetest.todo.models import Category

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('name')