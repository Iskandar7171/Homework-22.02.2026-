from rest_framework.viewsets import ModelViewSet
from .models import LessonFeedback, CourseFeedback
from .serializer import LessonFeedbackSerializer, CourseFeedbackSerializer

class LessonFeedbackViewSet(ModelViewSet):
    queryset = LessonFeedback.objects.all()
    serializer_class = LessonFeedbackSerializer

class CourseFeedbackViewSet(ModelViewSet):
    queryset = CourseFeedback.objects.all()
    serializer_class = CourseFeedbackSerializer
