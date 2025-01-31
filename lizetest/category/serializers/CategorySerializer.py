from rest_framework.serializers import ModelSerializer
from lizetest.category.models import Category

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('name')