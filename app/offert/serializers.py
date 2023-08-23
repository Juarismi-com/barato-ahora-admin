from rest_framework import routers, serializers, viewsets
from .models import Offert, OffertCategory

# Serializers
class OffertSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Offert
        fields = ['title', 'date_start', 'date_end']

class OffertCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OffertCategory
        fields = ['name']     


# ViewSets
class OffertViewSet(viewsets.ModelViewSet):
    queryset = Offert.objects.all()
    serializer_class = OffertSerializer

class OffertCategoryViewSet(viewsets.ModelViewSet):
    queryset = OffertCategory.objects.all()
    serializer_class = OffertCategorySerializer    
           

# Router
router = routers.DefaultRouter()
router.register(r'offerts', OffertViewSet)
router.register(r'offert-categories', OffertCategoryViewSet)