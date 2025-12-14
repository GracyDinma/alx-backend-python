from django.shortcuts import render
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer

# Create your views here.
class ConverationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.OrderingFilter]
    ordering = ["created_at"]
    
    def perform_create(self, serializer):
        conversation = serializer.save()
        conversation.participants.add(self.request.user)

    class MessageViewSet(viewsets.ModelViewSet):
        queryset = Message.objects.all()
        serializer_class = MessageSerializer
        permission_classes = [IsAuthenticated]
        filter_backends = [filters.OrderingFilter]
        ordering = ["sent_at"]
        
        def perform_create(self, serializer):
            serializer.save(sender=self.request.user)

