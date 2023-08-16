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
from offert.api import UserCompanyViewSet, CategoryViewSet, OffertTypeViewSet, OffertViewSet
from .serializers import router

urlpatterns = [
    path("offerts/", include("offert.urls")),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # Endpoint de usuarios de empresas
    path('api/usercompanies/', UserCompanyViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='usercompanies-list'),

    path('api/usercompanies/<int:pk>/', UserCompanyViewSet.as_view({
        'put': 'update',
        'delete': 'destroy'
    }), name='usercompanies-detail'),

    # Endpoint de categorias
    path('api/categories/', CategoryViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='categories-list'),

    path('api/categories/<int:pk>/', CategoryViewSet.as_view({
        'put': 'update',
        'delete': 'destroy'
    }), name='categories-detail'),


    # Endpoint de tipos de oferta
    path('api/offerttypes/', OffertTypeViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='offerttypes-list'),

    path('api/offerttypes/<int:pk>/', OffertTypeViewSet.as_view({
        'put': 'update',
        'delete': 'destroy'
    }), name='offerttypes-detail'),


    # Endpoint de ofertas
    path('api/offerts/', OffertViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='offerts-list'),

    path('api/offerts/<int:pk>/', OffertViewSet.as_view({
        'put': 'update',
        'delete': 'destroy'
    }), name='offerts-detail'),
]
