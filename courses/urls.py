from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, CourseViewSet, StudentCourseViewSet

router = DefaultRouter()
router.register("categories", CategoryViewSet)
router.register("courses", CourseViewSet)
router.register("student-courses", StudentCourseViewSet)

urlpatterns = router.urls
