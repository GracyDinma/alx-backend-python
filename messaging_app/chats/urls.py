from rest_framework.routers import DefaultRouter
from .views import ConversationViewSet, MessageViewSet

router = DefaultRouter()
router.register(r"conversation", ConversationViewSet, basename="converation")
router.register(r"messages", MessageViewSet, basename="message")

urlpatterns = router.urls
