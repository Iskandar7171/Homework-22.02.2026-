from rest_framework import serializers
from .models import LessonFeedback, CourseFeedback

class LessonFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonFeedback
        fields = "__all__"

class CourseFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseFeedback
        fields = "__all__"
