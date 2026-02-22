from rest_framework.routers import DefaultRouter
from .views import LessonFeedbackViewSet, CourseFeedbackViewSet

router = DefaultRouter()
router.register("lesson-feedbacks", LessonFeedbackViewSet)
router.register("course-feedbacks", CourseFeedbackViewSet)

urlpatterns = router.urls
