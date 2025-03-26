from rest_framework import generics, status
from rest_framework.response import Response
from .models import UserAnswer, UserTextfieldExerciseAnswer
from .serializers import DynamicUserAnswerSerializer, UserTextfieldExerciseAnswerSerializer
from rest_framework.views import APIView



class UserAnswerListView(generics.ListAPIView):
  queryset = UserAnswer.objects.all()
  serializer_class = DynamicUserAnswerSerializer

class UserTextfieldExerciseAnswerCreateView(generics.CreateAPIView):
    queryset = UserTextfieldExerciseAnswer.objects.all()
    serializer_class = UserTextfieldExerciseAnswerSerializer

# This is an example of custom View
class SpesificUserAnswerListView(APIView):
  
  def get(self, request, user, format=None):

    # Filter UserAnswer objects where 'user' field matches the given username
    user_answers = UserAnswer.objects.filter(user=user)  # Exact match

    if not user_answers.exists():
      return Response({"error": "No answers found for this user."}, status=status.HTTP_404_NOT_FOUND)

    serializer = DynamicUserAnswerSerializer(user_answers, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
  

class SpesificExerciseAnswerListView(APIView):
  
  def get(self, request, exercise, format=None):

    # Filter UserAnswer objects where 'user' field matches the given username
    user_answers = UserAnswer.objects.filter(exercise=exercise)  # Exact match

    if not user_answers.exists():
      return Response({"error": "No answers found for this exercise."}, status=status.HTTP_404_NOT_FOUND)

    serializer = DynamicUserAnswerSerializer(user_answers, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
