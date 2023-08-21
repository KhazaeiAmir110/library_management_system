from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from user.models import User
from user.serializers import UserBackOfficeSerializer


class UserBackOfficeViewSet(mixins.ListModelMixin,
                            mixins.CreateModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserBackOfficeSerializer
