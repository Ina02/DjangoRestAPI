from rest_framework import serializers
from .models import Course

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ('id','url','name','language','price')

#To add the url of each of the course in the dictionary as a key-value pair, we use HyperlinkedModelSerializer instead of just ModelSerializer
