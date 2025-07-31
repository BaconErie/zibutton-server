from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, mixins
from .models import List, Progress
from .serializers import ListSerializer, ProgressSerializer
from django.db.models import Q
from .permissions import RestrictEditPermission, RestrictCreatePermission

class ListViewSet(viewsets.GenericViewSet,
               mixins.CreateModelMixin,
               mixins.RetrieveModelMixin,
               mixins.UpdateModelMixin,
               mixins.DestroyModelMixin,
               ):
    
    serializer_class = ListSerializer
    permission_classes = [RestrictEditPermission, RestrictCreatePermission]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return List.objects.filter(
                Q(owner=self.request.user) | Q(is_public=True)
            )
        else:
            return List.objects.filter(is_public=True)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
