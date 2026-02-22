from django.db import models
from lessons.models import Lesson
from courses.models import Course
from users.models import User


class LessonFeedback(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    star = models.IntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True)


class CourseFeedback(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    star = models.IntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True)