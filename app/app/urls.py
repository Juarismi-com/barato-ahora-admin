"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .serializers import UserViewSet
from offert.serializers import OffertViewSet, OffertCategoryViewSet, CategoryViewSet  
from rest_framework import routers

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'offerts', OffertViewSet,basename='offert')
router.register(r'offert-categories', OffertCategoryViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
   path('admin/', admin.site.urls),
   path('api/', include([
      path('', include(router.urls)),     
      path('auth/', include('authentication.urls'))
   ]))
]
