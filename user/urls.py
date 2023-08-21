from django.conf.urls import include
from django.urls import path
from .views import UserBackOfficeViewSet
from rest_framework import routers

backoffice_router = routers.SimpleRouter()
backoffice_router.register(r'backoffice', UserBackOfficeViewSet)

urlpatterns = [
    path('', include(backoffice_router.urls)),
]
