from rest_framework.viewsets import ModelViewSet
from .models import Module, Lesson, StudentLessonProgress
from .serializer import ModuleSerializer, LessonSerializer, ProgressSerializer

class ModuleViewSet(ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer

class LessonViewSet(ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class ProgressViewSet(ModelViewSet):
    queryset = StudentLessonProgress.objects.all()
    serializer_class = ProgressSerializer
