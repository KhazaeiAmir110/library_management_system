from django.conf.urls import include
from django.urls import path
from .views import (
    ReservationViewSet, UserReservationListAPIView
)
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'create', ReservationViewSet, basename='create-user')
router.register(r'list', UserReservationListAPIView, basename='list')

urlpatterns = [
    path('', include(router.urls)),
]
