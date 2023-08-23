from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, status, generics
from .models import ReservationTest
from .serializers import (
    ReservationCreateOutputSerializer, ReservationListSerializer, ReservationCreateInputSerializer
)
from rest_framework.permissions import IsAuthenticated


class ReservationViewSet(mixins.CreateModelMixin,
                         GenericViewSet):
    queryset = ReservationTest.objects.filter()
    serializer_class = ReservationCreateOutputSerializer
    lookup_field = 'id'
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = ReservationCreateInputSerializer(
            data=dict(
                user=request.user.id,
                documentation=request.data.get('documentation')
            )
        )
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        reservation_serializer = ReservationCreateOutputSerializer(serializer.instance)

        headers = self.get_success_headers(reservation_serializer.data)
        return Response(reservation_serializer.data, status=status.HTTP_201_CREATED,
                        headers=headers)


class UserReservationListAPIView(mixins.ListModelMixin, GenericViewSet):
    serializer_class = ReservationListSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return ReservationTest.objects.filter(user=user)
