from django.http import Http404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Notes
from .serializers import NoteSerializer
# Create your views here.

class NoteList(APIView):
    def get(self, request):
        notas = Notes.objects.all()
        serializer = NoteSerializer(notas, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NoteDetail(APIView):
    def get_object(self, pk):
        try:
            return Notes.objects.get(pk=pk)
        except Notes.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        nota = self.get_object(pk)
        serializer = NoteSerializer(nota)
        return Response(serializer.data)

    def put(self, request, pk):
        nota = self.get_object(pk)
        serializer = NoteSerializer(nota, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        nota = self.get_object(pk)
        nota.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
