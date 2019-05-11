from rest_framework.views import APIView
from django.http.response import HttpResponse, JsonResponse

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from .models import Note
from .serializers import NoteSerializer


class NotesList(APIView):
    """
        List all snippets, or create a new snippet.
    """

    def get(self, request, format=None):
        snippets = Note.objects.all().order_by('-date')
        serializer = NoteSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        print(str(request.data))
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            print('dsogjh')
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NoteDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Note.objects.get(pk=pk)
        except Note.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = NoteSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        print(request.data)
        snippet = self.get_object(pk)
        serializer = NoteSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



