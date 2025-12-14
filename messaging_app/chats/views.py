from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer

# Create your views here.
class ConverationViewSet(viewsets.ModelViewSet):
    serializer_class = ConversationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Conversation.objects.filter(
            participants=self.request.user
        ).distinct()
    
    def perform_create(self, serializer):
        conversation = serializer.save()
        conversation.participants.add(self.request.user)

    class MessageViewSet(viewsets.ModelViewSet):
        serializer_class = MessageSerializer
        permission_classes = [IsAuthenticated]

        def get_query(self):
            conversation_id = self.request.query_params.get("conversation")
            qs = Message.objects.all()

            if conversation_id:
                qs = qs.filter(conversation_id=conversation_id)

            return qs.order_by("sent_at")
        
        def perform_create(self, serializer):
            serializer.save(sender=self.request.user)

