from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response

from .models import Evaluation
from user_answer.models import UserAnswer
from .serializers import EvaluationSerializer

class EvaluationList(generics.ListAPIView):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer

class EvaluationListByStaff(generics.ListAPIView):
    serializer_class = EvaluationSerializer

    def get_queryset(self):
        user = self.kwargs['user']
        return Evaluation.objects.filter(user=user)

class EvaluationCreate(generics.CreateAPIView):
    serializer_class = EvaluationSerializer

    def create(self, request, *args, **kwargs):
        answer_id = self.kwargs['answer']
        user_answer = get_object_or_404(UserAnswer, pk=answer_id)

        if user_answer.evaluation:
            return Response({"error": "Evaluation already exists for this answer."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            evaluation = serializer.save()
            user_answer.evaluation = evaluation
            user_answer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
class EvaluationRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer
    lookup_field = 'id'
