from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Homework, HomeworkSubmission
from .serializer import HomeworkSerializer, SubmissionSerializer

class HomeworkViewSet(ModelViewSet):
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializer

class SubmissionViewSet(ModelViewSet):
    queryset = HomeworkSubmission.objects.all()
    serializer_class = SubmissionSerializer
