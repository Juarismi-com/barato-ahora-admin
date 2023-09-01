from rest_framework import routers, serializers, viewsets, filters
from django.db.models import Q
from .models import Offert, OffertCategory, Category

# Serializers
class OffertSerializer(serializers.HyperlinkedModelSerializer):
    business_receptor = serializers.StringRelatedField()
    offert_type = serializers.StringRelatedField()
    offert_category = serializers.StringRelatedField()
    user_created = serializers.StringRelatedField()

    class Meta:
        model = Offert
        fields = ['title', 'date_start', 'date_end', 'description', 'disclaimer', 'active',
                  'discount_rate', 'business_receptor', 'offert_type', 'offert_category', 'user_created']


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


# Router
router = routers.DefaultRouter()
router.register(r'offerts', OffertViewSet, basename='offert')
router.register(r'offert-categories', OffertCategoryViewSet)
router.register(r'categories', CategoryViewSet)
