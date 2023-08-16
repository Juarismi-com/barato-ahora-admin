from rest_framework import serializers
from .models import Category

#Categorias
class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = '__all__'
    read_only_fields = ('created_at',)
    
