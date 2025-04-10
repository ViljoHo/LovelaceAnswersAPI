from django.shortcuts import get_object_or_404
from django.urls import reverse
from rest_framework import generics

from api_keys.permissions import HasAPIKeyPermission
from user_answer.models import UserAnswer
from .models import Evaluation
from .serializers import EvaluationSerializer


class EvaluationList(generics.ListAPIView):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer
    permission_classes = [HasAPIKeyPermission]


class EvaluationListByStaff(generics.ListAPIView):
    serializer_class = EvaluationSerializer
    permission_classes = [HasAPIKeyPermission]

    def get_queryset(self):
        user = self.kwargs["user"]
        return Evaluation.objects.filter(evaluator=user)


class EvaluationRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EvaluationSerializer
    permission_classes = [HasAPIKeyPermission]

    def get_object(self):
        answer_id = self.kwargs["answer"]
        user_answer = get_object_or_404(UserAnswer, pk=answer_id)

        if not user_answer.evaluation and self.request.method in ["PUT"]:
            evaluation = Evaluation.objects.create()
            user_answer.evaluation = evaluation
            user_answer.save()
        else:
            evaluation = user_answer.evaluation

        return user_answer.evaluation
