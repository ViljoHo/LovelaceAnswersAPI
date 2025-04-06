from rest_framework import generics
from django.urls import reverse
from rest_framework.response import Response
from rest_framework import status
from .serializers import (
    DynamicUserAnswerSerializer,
    UserCheckboxExerciseAnswerSerializer,
    UserTextfieldExerciseAnswerSerializer,
    UserMultipleChoiceExerciseAnswerSerializer,
    UserMultipleQuestionExamAnswerSerializer,
)
from api_keys.permissions import HasAPIKeyPermission

from .models import (
    UserAnswer,
    UserCheckboxExerciseAnswer,
    UserTextfieldExerciseAnswer,
    UserMultipleChoiceExerciseAnswer,
    UserMultipleQuestionExamAnswer,
)


class AnswerList(generics.ListAPIView):
    queryset = UserAnswer.objects.all()
    serializer_class = DynamicUserAnswerSerializer
    permission_classes = [HasAPIKeyPermission]


class BaseExerciseAnswerCreateView(generics.CreateAPIView):
    permission_classes = [HasAPIKeyPermission]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()

        location_url = reverse("get-delete-answer", kwargs={"id": instance.id})

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers={"Location": location_url},
        )


class UserTextfieldExerciseAnswerCreate(BaseExerciseAnswerCreateView):
    queryset = UserTextfieldExerciseAnswer.objects.all()
    serializer_class = UserTextfieldExerciseAnswerSerializer


class UserMultipleChoiceExerciseAnswerCreate(BaseExerciseAnswerCreateView):
    queryset = UserMultipleChoiceExerciseAnswer.objects.all()
    serializer_class = UserMultipleChoiceExerciseAnswerSerializer


class UserMultipleQuestionExamAnswerCreate(BaseExerciseAnswerCreateView):
    queryset = UserMultipleQuestionExamAnswer.objects.all()
    serializer_class = UserMultipleQuestionExamAnswerSerializer


class UserCheckboxExerciseAnswerCreate(BaseExerciseAnswerCreateView):
    queryset = UserCheckboxExerciseAnswer.objects.all()
    serializer_class = UserCheckboxExerciseAnswerSerializer


class AnswerListByUser(generics.ListAPIView):
    serializer_class = DynamicUserAnswerSerializer
    permission_classes = [HasAPIKeyPermission]

    def get_queryset(self):
        user = self.kwargs["user"]
        return UserAnswer.objects.filter(user=user)


class AnswerListByExercise(generics.ListAPIView):
    serializer_class = DynamicUserAnswerSerializer
    permission_classes = [HasAPIKeyPermission]

    def get_queryset(self):
        exercise = self.kwargs["exercise"]
        return UserAnswer.objects.filter(exercise=exercise)


class AnswerListByCourse(generics.ListAPIView):
    serializer_class = DynamicUserAnswerSerializer
    permission_classes = [HasAPIKeyPermission]

    def get_queryset(self):
        course = self.kwargs["course"]
        return UserAnswer.objects.filter(instance=course)


class AnswerListByUserAndExercise(generics.ListAPIView):
    serializer_class = DynamicUserAnswerSerializer
    permission_classes = [HasAPIKeyPermission]

    def get_queryset(self):
        user = self.kwargs["user"]
        exercise = self.kwargs["exercise"]
        return UserAnswer.objects.filter(user=user, exercise=exercise)


class AnswerListByUserAndCourse(generics.ListAPIView):
    serializer_class = DynamicUserAnswerSerializer
    permission_classes = [HasAPIKeyPermission]

    def get_queryset(self):
        user = self.kwargs["user"]
        course = self.kwargs["course"]
        return UserAnswer.objects.filter(user=user, instance=course)


class AnswerRetrieveDestroy(generics.RetrieveDestroyAPIView):
    queryset = UserAnswer.objects.all()
    serializer_class = DynamicUserAnswerSerializer
    permission_classes = [HasAPIKeyPermission]
    lookup_field = "id"
