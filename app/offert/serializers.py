from rest_framework import serializers, viewsets
from .models import Offert, OffertCategory, Category

# Serializers
class OffertSerializer(serializers.HyperlinkedModelSerializer):
    business_receptor = serializers.StringRelatedField()
    offert_type = serializers.StringRelatedField()
    offert_category = serializers.StringRelatedField()
    user_created = serializers.StringRelatedField()

    class Meta:
        model = Offert
        fields = '__all__'


class OffertCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OffertCategory
        fields = ['id', 'name']


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class OffertViewSet(viewsets.ModelViewSet):
    serializer_class = OffertSerializer

    def get_queryset(self):
        queryset = Offert.objects.all()
        offert_category_id = self.request.query_params.get('offert_category_id') 

        if offert_category_id:          
            queryset = queryset.filter(offert_category_id=offert_category_id)

        return queryset


class OffertCategoryViewSet(viewsets.ModelViewSet):
    queryset = OffertCategory.objects.all()
    serializer_class = OffertCategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

