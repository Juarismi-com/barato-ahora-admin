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
from .api import UserCompanyViewSet, CategoryViewSet, OffertTypeViewSet, OffertViewSet

router = routers.DefaultRouter()

router.register('api/usercompanies', UserCompanyViewSet, 'usercompanies')
router.register('api/categories', CategoryViewSet, 'categories')
router.register('api/offerttypes', OffertTypeViewSet, 'offerttypes')
router.register('api/offerts', OffertViewSet, 'offerts')

urlpatterns = router.urls
