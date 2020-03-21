from django.shortcuts import render
from rest_framework import viewsets
from courses.models import Course
from courses.serializer import CourseSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer