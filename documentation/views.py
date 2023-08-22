from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, filters
from .models import Documentation
from .serializers import DocumentationSerializer
from django_filters.rest_framework import DjangoFilterBackend
from core.pagination import CustomPagination
import core.redis_services as redis_services
from rest_framework.response import Response
import json


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

    def list(self, request, *args, **kwargs):
        documentation_list = redis_services.get('documentation_list')
        if documentation_list:
            return Response(json.loads(documentation_list))

        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        redis_services.set('documentation_list', json.dumps(serializer.data))
        return Response(serializer.data)


class DocumentationBackOfficeViewSet(mixins.ListModelMixin,
                                     mixins.CreateModelMixin,
                                     mixins.RetrieveModelMixin,
                                     mixins.UpdateModelMixin,
                                     mixins.DestroyModelMixin,
                                     GenericViewSet):
    queryset = Documentation.objects.all()
    serializer_class = DocumentationSerializer
    lookup_field = 'id'

    def list(self, request, *args, **kwargs):
        documentation_list = redis_services.get('documentation_list')
        if documentation_list:
            return Response(json.loads(documentation_list))

        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        redis_services.set('documentation_list', json.dumps(serializer.data))
        return Response(serializer.data)
