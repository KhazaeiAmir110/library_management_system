from rest_framework import serializers
from .models import ReservationTest


class ReservationListSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username', read_only=True)
    documentation_name = serializers.CharField(source='documentation.name', read_only=True)

    class Meta:
        model = ReservationTest
        fields = (
            'id', 'user_name', 'documentation_name', 'created', 'pyment')


class ReservationCreateOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservationTest
        fields = (
            'id', 'user', 'documentation', 'created', 'updated', 'pyment'
        )


class ReservationCreateInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservationTest
        fields = ('documentation', 'user')
