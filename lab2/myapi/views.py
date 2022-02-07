from django.http import HttpResponse, JsonResponse
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework import viewsets, authentication, permissions
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from rest_framework import generics
from myapi.serializers import Studentserializers, Trackserializers
from students.models import Student, Track
from rest_framework.response import Response
from rest_framework import status, mixins


# with class based
class StudentAPI(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = Studentserializers(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Studentserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# with function based
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


class Student_DetailsAPI(APIView):
    def get_object(self, id):
        try:
            return Student.objects.get(id=id)
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        student = self.get_object(id)
        serializer = Studentserializers(student)
        return Response(serializer.data)

    def put(self, request, id):
        student = self.get_object(id)
        serializer = Studentserializers(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        student = self.get_object(id)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
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


class GenericStudentAPI(generics.ListCreateAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = Studentserializers

    def list(self, request):
        queryset = self.get_queryset()
        serializer = Studentserializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        return self.create(request)


class GenericStudentdetailsAPI(generics.ListCreateAPIView, mixins.ListModelMixin, mixins.DestroyModelMixin,
                               mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    queryset = Student.objects.all()
    serializer_class = Studentserializers
    lookup_field = 'id'

    def list(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def update(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id=None):
        return self.delete(request, id)


class StudentViewSet(viewsets.ViewSet):
    queryset = Student.objects.all()
    serializer_class = Studentserializers


class Tracklist(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = Trackserializers
