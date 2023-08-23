from rest_framework import routers, serializers, viewsets
from .models import Offert, OffertCategory, Category

# Serializers
class OffertSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Offert
        fields = ['title', 'date_start']

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['name']     


# ViewSets
class OffertViewSet(viewsets.ModelViewSet):
    queryset = Offert.objects.all()
    serializer_class = OffertSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer    
           

# Router
router = routers.DefaultRouter()

router.register(r'api/offerts', OffertViewSet)
router.register(r'api/categories', CategoryViewSet)