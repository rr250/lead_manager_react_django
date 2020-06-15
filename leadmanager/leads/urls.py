from rest_framework import routers
from django.urls import path
from .api import LeadViewSet
from .api import Search

router = routers.DefaultRouter()
router.register('api/leads', LeadViewSet, 'leads')

urlpatterns = [
    path('api/leads/search', Search.as_view()),
]

urlpatterns += router.urls