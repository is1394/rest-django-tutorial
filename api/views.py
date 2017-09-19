from rest_framework import viewsets

from .models import Notes
from .serializers import NoteSerializer
# Create your views here.
class NoteViewSet(viewsets.ModelViewSet):
    queryset = Notes.objects.all()
    serializer_class = NoteSerializer
    