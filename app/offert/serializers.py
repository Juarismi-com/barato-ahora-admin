from rest_framework import routers, serializers, viewsets
from .models import Offert, Category, OffertCategory

# Serializers
class OffertSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Offert
        fields = ['title', 'date_start']

class OffertCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OffertCategory
        fields = ['name']        

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['name']        


# ViewSets
class OffertViewSet(viewsets.ModelViewSet):
    queryset = Offert.objects.all()
    serializer_class = OffertSerializer

class OffertCategoryViewSet(viewsets.ModelViewSet):
    queryset = OffertCategory.objects.all()
    serializer_class = OffertCategorySerializer        

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer    
   

# Routers
router = routers.DefaultRouter()
router.register(r'api/offerts', OffertViewSet)
router.register(r'api/offertcategories', OffertCategoryViewSet)
router.register(r'api/categories', CategoryViewSet)

