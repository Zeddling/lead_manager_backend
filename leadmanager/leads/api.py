from .models import Lead
from .serializers import LeadSerializers
from rest_framework import viewsets, permissions


class LeadViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = LeadSerializers

    #   returns all leads belonging to user
    def get_queryset(self):
        return self.request.user.leads.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
