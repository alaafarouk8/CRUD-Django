from django.http import HttpResponse, JsonResponse
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from myapi.serializers import Studentserializers, Trackserializers
from students.models import Student, Track
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def student_list(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = Studentserializers(students, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = Studentserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT' , 'DELETE'])
def student_detail(request, pk):
    try:
        students = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Studentserializers(students)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = Studentserializers(students, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        students.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Tracklist(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = Trackserializers
