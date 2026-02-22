from rest_framework.routers import DefaultRouter
from .views import ModuleViewSet, LessonViewSet, ProgressViewSet

router = DefaultRouter()
router.register("modules", ModuleViewSet)
router.register("lessons", LessonViewSet)
router.register("progress", ProgressViewSet)

urlpatterns = router.urls
