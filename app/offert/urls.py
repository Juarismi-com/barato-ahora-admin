# from django.urls import path
# from . import views

# urlpatterns = [
#     path("", views.index, name="index"),
#     # ex: /polls/5/
#     path("<int:question_id>/", views.detail, name="detail"),
#     # ex: /polls/5/results/
#     path("<int:question_id>/results/", views.results, name="results"),
#     # ex: /polls/5/vote/
# ]

from rest_framework import routers
from .api import CategoryViewSet

router = routers.DefaultRouter()

router.register('api/categories', CategoryViewSet, 'categories')

urlpatterns = router.urls


