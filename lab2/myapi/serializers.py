from rest_framework import serializers

from students.models import Track, Student


class Trackserializers(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = '__all__'


class Studentserializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
