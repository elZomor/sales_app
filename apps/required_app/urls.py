from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.required_app.views import SegmentViewSet

router = DefaultRouter()
router.register("segments", SegmentViewSet, basename="heel")
urlpatterns = router.urls
