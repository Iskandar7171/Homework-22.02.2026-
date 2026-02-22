from rest_framework.viewsets import ModelViewSet
from .models import Category, Course, StudentCourse
from .serializer import (
CategorySerializer,
CourseSerializer,
StudentCourseSerializer
)

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class StudentCourseViewSet(ModelViewSet):
    queryset = StudentCourse.objects.all()
    serializer_class = StudentCourseSerializer
