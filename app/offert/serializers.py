from rest_framework import routers, serializers, viewsets
from .models import Offert

class OffertSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Offert
        fields = ['title', 'date_start']

# ViewSets
class OffertViewSet(viewsets.ModelViewSet):
    queryset = Offert.objects.all()
    serializer_class = OffertSerializer
   

# Routers
router = routers.DefaultRouter()
router.register(r'api/offerts', OffertViewSet)


