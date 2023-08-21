from rest_framework import serializers
from .models import Documentation


class DocumentationSerializer(serializers.ModelSerializer):
    type_display = serializers.SerializerMethodField()
    status_display = serializers.SerializerMethodField()

    class Meta:
        model = Documentation
        fields = (
            'id', 'name', 'author', 'genre', 'city', 'type_display', 'status_display',
            'description', 'price'
        )

    def get_type_display(self, obj):
        return obj.get_type_display()

    def get_status_display(self, obj):
        return obj.get_status_display()
