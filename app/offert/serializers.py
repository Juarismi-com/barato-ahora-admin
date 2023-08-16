from rest_framework import routers, serializers, viewsets
from .models import Offert, OffertCategory
class OffertSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Offert
        fields = ['title','date_start']


class OffertCategorySeriealizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OffertCategory
        fields = ['name']


router = routers.DefaultRouter()
router.register('r/offerts')