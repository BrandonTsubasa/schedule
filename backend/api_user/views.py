from django.shortcuts import render
from rest_framework import generics, permissions
from api_user import serializers
from core.models import User
# from core.models import GuestUser
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated


from django.db import IntegrityError
from rest_framework.exceptions import ValidationError


class CreateUserView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()


class ListUserView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class DeleteUserView(generics.DestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class ManageUserView(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

    def get_object(self):
        return self.request.user
