from rest_framework.routers import routers
from .views import ConversationViewSet, MessageViewSet
from django.urls import path, include


router = routers.DefaultRouter()
router.register(r"conversation", ConversationViewSet, basename="converation")
router.register(r"messages", MessageViewSet, basename="message")

urlpatterns = [
    path("", include(router.urls)),
]
