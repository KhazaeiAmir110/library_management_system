from django.conf.urls import include
from django.urls import path
from .views import DocumentationViewSet, DocumentationBackOfficeViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', DocumentationViewSet)

backoffice_router = routers.SimpleRouter()
backoffice_router.register(r'', DocumentationBackOfficeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('back_office/', include(backoffice_router.urls))
]
