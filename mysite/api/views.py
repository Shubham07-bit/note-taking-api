from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Note
from .serializers import NoteSerializer
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class NoteListCreate(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    @swagger_auto_schema(
        operation_description="Create a new note",
        responses={201: NoteSerializer}
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class NoteRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    lookup_field = "pk"

    @swagger_auto_schema(
        operation_description="Retrieve, update or delete a note by ID",
        responses={200: NoteSerializer}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class NoteList(APIView):
    def get(self, request, format=None):
        # Get the title from the query parameters(if none, default to empty string)
        title = request.query_params.get("title", "")

        if title:
            # Filter the queryset based on the title
            notes = Note.objects.filter(title__icontains=title)
        else:
            # If no title is provided, return all notes
            notes = Note.objects.all()

        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
