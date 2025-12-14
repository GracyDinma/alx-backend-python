from rest_framework.routers import routers
from .views import ConversationViewSet, MessageViewSet
from django.urls import path, include
from rest_framework_nested.routers import NestedDefaultRouter


router = routers.DefaultRouter()
router.register(r"conversation", ConversationViewSet, basename="conversation")
conversations_router = NestedDefaultRouter(
    router,
    r"conversations",
    lookup="conversation"
)

conversations_router.register(
    r"messages",
    MessageViewSet,
    basename="conversation-messages"
)

urlpatterns = [
    path("", include(router.urls)),
    path("", include(conversations_router.urls)),
]
