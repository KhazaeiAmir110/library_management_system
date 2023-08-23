from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from core.throttling import UserPhoneRateThrottle
from .models import User
import core.services as core_services
import user.services as user_services
from .serializers import (
    UserPublicSerializer, UserBackOfficeSerializer, UserGenerateOTPSerializer, VeryfiSerializer,
    UserVerifyOTPSerializer, CustomTokenObtainPairSerializer
)


class UserBackOfficeViewSet(mixins.ListModelMixin,
                            mixins.CreateModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserBackOfficeSerializer


class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserPublicSerializer
    throttle_classes = [UserPhoneRateThrottle]
    throttle_scope = 'user'

    @action(methods=['POST'], detail=False, url_path='generate-otp')
    def generate_otp(self, request, *args, **kwargs):
        serializer = UserGenerateOTPSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        otp_code = core_services.create_otp(serializer.validated_data.get('phone_number'))

        return Response(dict(otp_code=otp_code))

    @action(methods=['POST'], detail=False, url_path='verify-otp')
    def verify_otp(self, request, *args, **kwargs):
        serializer = UserVerifyOTPSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        otp_code = serializer.validated_data.get('otp_code')
        phone_number = serializer.validated_data.get('phone_number')
        if core_services.is_otp_match(otp_code, phone_number):
            user = user_services.get_user(phone_number=phone_number)
            data = dict()
            if not user:
                user = user_services.create_user(
                    phone_number=phone_number, username=phone_number
                )
                serializer = CustomTokenObtainPairSerializer(
                    data=dict(username=user.username)
                )
                serializer.is_valid(raise_exception=True)
                data = serializer.validated_data
            else:
                serializer = CustomTokenObtainPairSerializer(
                    data=dict(username=user.username)
                )
                serializer.is_valid(raise_exception=True)
                data = serializer.validated_data

            return Response(data)

        raise ValidationError()
