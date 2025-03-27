from rest_framework import generics
from .serializers import (
    DynamicUserAnswerSerializer,
    UserTextfieldExerciseAnswerSerializer,
)
from api_keys.permissions import HasAPIKeyPermission

from .models import UserAnswer, UserTextfieldExerciseAnswer

class AnswerList(generics.ListAPIView):
    queryset = UserAnswer.objects.all()
    serializer_class = DynamicUserAnswerSerializer
    permission_classes = [HasAPIKeyPermission]


class UserTextfieldExerciseAnswerCreate(generics.CreateAPIView):
    queryset = UserTextfieldExerciseAnswer.objects.all()
    serializer_class = UserTextfieldExerciseAnswerSerializer
    permission_classes = [HasAPIKeyPermission]


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


class SpecificAnswer(generics.RetrieveDestroyAPIView):
    queryset = UserAnswer.objects.all()
    serializer_class = DynamicUserAnswerSerializer
    permission_classes = [HasAPIKeyPermission]
    lookup_field = "id"


# This is an example of custom View
# class AnswerListViewByUser(APIView):

#   def get(self, request, user, format=None):

#     # Filter UserAnswer objects where 'user' field matches the given username
#     user_answers = UserAnswer.objects.filter(user=user)  # Exact match

#     if not user_answers.exists():
#       return Response({"error": "No answers found for this user."}, status=status.HTTP_404_NOT_FOUND)

#     serializer = DynamicUserAnswerSerializer(user_answers, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)
