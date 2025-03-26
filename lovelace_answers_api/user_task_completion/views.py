from django.shortcuts import render
from rest_framework import generics
from .models import UserTaskCompletion
from .serializers import UserTaskCompletionSerializer


class UserTaskCompletionListCreate(generics.ListCreateAPIView):
    queryset = UserTaskCompletion.objects.all()
    serializer_class = UserTaskCompletionSerializer
