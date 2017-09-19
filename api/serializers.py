from rest_framework import serializers
from .models import Notes

class NoteSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Notes
        fields = ('id', 'title', 'body')
        read_only_fields = ('date_created', 'date_modificated')