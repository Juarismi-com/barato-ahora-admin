from rest_framework import serializers
from .models import UserCompany, Category, OffertType, Offert


# Usuarios de empresa
class UserCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCompany
        fields = '__all__'
        read_only_fields = ('created_at',)


# Categorias
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ('created_at',)


# Tipo de Ofertas
class OffertTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OffertType
        fields = '__all__'
        read_only_fields = ('created_at',)


# Ofertas
class OffertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offert
        fields = '__all__'
        read_only_fields = ('created_at',)
