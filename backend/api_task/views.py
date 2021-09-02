from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes, authentication_classes
from core.models import Task
from api_task import serializers
from rest_framework.response import Response


class ListTaskView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = serializers.TaskSerializer
    permission_classes = (permissions.IsAuthenticated, )


class CreateTaskView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = serializers.TaskSerializer
    permission_classes = (permissions.IsAuthenticated, )


class RetrieveUpdateDestroyTaskView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = serializers.TaskSerializer
    permission_classes = (permissions.IsAuthenticated, )
