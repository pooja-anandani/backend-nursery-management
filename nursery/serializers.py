from rest_framework import serializers
from nursery.models import Plant


# Plant serializer

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        exclude = ('is_deleted', 'modified_at', 'created_at',)
