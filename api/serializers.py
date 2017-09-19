from rest_framework import serializers
from .models import Notes

class NoteSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Notes
        fields = ('id', 'title', 'body', 'owner')
        read_only_fields = ('date_created', 'date_modificated')