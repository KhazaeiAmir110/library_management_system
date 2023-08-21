from django.conf.urls import include
from django.urls import path
from .views import UserBackOfficeViewSet, UserViewSet
from rest_framework import routers

backoffice_router = routers.SimpleRouter()
backoffice_router.register(r'backoffice', UserBackOfficeViewSet)

router = routers.DefaultRouter()
router.register(r'', UserViewSet)

urlpatterns = [
    path('', include(backoffice_router.urls)),
    path('', include(router.urls)),
]
