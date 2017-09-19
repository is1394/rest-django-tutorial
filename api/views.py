from rest_framework import viewsets
from rest_framework import permissions

from .models import Notes
from .serializers import NoteSerializer
from .permissions import IsOwner
# Create your views here.
class NoteViewSet(viewsets.ModelViewSet):
    queryset = Notes.objects.all()
    serializer_class = NoteSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner,)

    def perform_create(self, serializer):
            serializer.save(owner=self.request.user)
    