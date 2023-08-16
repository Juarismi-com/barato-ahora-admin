from offert.models import UserCompany, Category, OffertType, Offert
from rest_framework import viewsets, permissions
from .serializers import UserCompanySerializer, CategorySerializer, OffertTypeSerializer, OffertSerializer

# Usuarios de empresa
class UserCompanyViewSet(viewsets.ModelViewSet):
    queryset = UserCompany.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserCompanySerializer

# Categorias
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CategorySerializer

# Tipo de ofertas
class OffertTypeViewSet(viewsets.ModelViewSet):
    queryset = OffertType.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = OffertTypeSerializer

# Ofertas
class OffertViewSet(viewsets.ModelViewSet):
    queryset = Offert.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = OffertSerializer
