from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.exceptions import NotFound

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

        if self.request.method == "PUT":
            # Create evaluation if it doesn't exist
            if not user_answer.evaluation:
                evaluation = Evaluation.objects.create()
                user_answer.evaluation = evaluation
                user_answer.save()
            return user_answer.evaluation

        # GET, DELETE and HEAD
        if not user_answer.evaluation:
            raise NotFound("Evaluation not found for this answer.")
        return user_answer.evaluation


class EvaluationDestroy(generics.DestroyAPIView):
    """
    Use to delete Evaluation if connected UserAnswer already deleted
    """

    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer
    permission_classes = [HasAPIKeyPermission]
    lookup_field = "id"
