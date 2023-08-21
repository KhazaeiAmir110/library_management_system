from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, filters
from .models import Documentation
from .serializers import DocumentationSerializer
from django_filters.rest_framework import DjangoFilterBackend
from core.pagination import CustomPagination


class DocumentationViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Documentation.objects.all()
    serializer_class = DocumentationSerializer

    search_fields = ['name', 'description', ]
    filterset_fields = ['type', 'status', 'genre', 'city', ]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter,
                       filters.OrderingFilter,
                       ]
    ordering_fields = ['name', 'author', 'price', ]

    pagination_class = CustomPagination


class DocumentationBackOfficeViewSet(mixins.ListModelMixin,
                                     mixins.CreateModelMixin,
                                     mixins.RetrieveModelMixin,
                                     mixins.UpdateModelMixin,
                                     mixins.DestroyModelMixin,
                                     GenericViewSet):
    queryset = Documentation.objects.all()
    serializer_class = DocumentationSerializer
    lookup_field = 'id'
