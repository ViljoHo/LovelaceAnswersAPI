from django.shortcuts import get_object_or_404
from django.urls import reverse
from rest_framework import generics, status
from rest_framework.response import Response

from .models import Evaluation
from api_keys.permissions import HasAPIKeyPermission
from user_answer.models import UserAnswer
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


class EvaluationCreate(generics.CreateAPIView):
    serializer_class = EvaluationSerializer
    permission_classes = [HasAPIKeyPermission]

    def create(self, request, *args, **kwargs):
        answer_id = self.kwargs["answer"]
        user_answer = get_object_or_404(UserAnswer, pk=answer_id)

        if user_answer.evaluation:
            return Response(
                {"error": "Evaluation already exists for this answer."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            evaluation = serializer.save()
            user_answer.evaluation = evaluation
            user_answer.save()

            location_url = reverse(
                "get-put-patch-delete-evaluation",
                kwargs={"id": evaluation.id},
            )

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
                headers={"Location": location_url},
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EvaluationRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer
    lookup_field = "id"
    permission_classes = [HasAPIKeyPermission]
