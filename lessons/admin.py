from django.contrib import admin
from .models import Module,Lesson,StudentLessonProgress
admin.site.register(Module)
admin.site.register(Lesson)
admin.site.register(StudentLessonProgress)