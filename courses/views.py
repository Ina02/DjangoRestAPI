from django.shortcuts import render
from rest_framework import viewsets
from .models import Course
from .serializers import CourseSerializer
# Create your views here.

class CourseView (viewsets.ModelViewSet):
    queryset = Course.objects.all()       #This is the model,the database
    serializer_class = CourseSerializer