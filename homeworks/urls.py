from rest_framework.routers import DefaultRouter
from .views import HomeworkViewSet, SubmissionViewSet

router = DefaultRouter()
router.register("homeworks", HomeworkViewSet)
router.register("submissions", SubmissionViewSet)

urlpatterns = router.urls
