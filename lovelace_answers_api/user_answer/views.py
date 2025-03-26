from rest_framework import generics, status
from rest_framework.response import Response
from .models import UserAnswer
from .serializers import DynamicUserAnswerSerializer
from rest_framework.views import APIView



class UserAnswerList(generics.ListAPIView):
  queryset = UserAnswer.objects.all()
  serializer_class = DynamicUserAnswerSerializer
