from django.urls import reverse
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import UserTaskCompletion
from .serializers import UserTaskCompletionSerializer

from api_keys.permissions import HasAPIKeyPermission
from .utils import MultipleFieldLookupMixin


class UserTaskCompletionListCreate(generics.ListCreateAPIView):
    queryset = UserTaskCompletion.objects.all()
    serializer_class = UserTaskCompletionSerializer
    permission_classes = [HasAPIKeyPermission]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        completion = serializer.save()

        location_url = reverse(
            "get-put-patch-delete-completion",
            kwargs={
                "user": completion.user,
                "exercise": completion.exercise,
                "instance": completion.instance,
            },
        )

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers={"Location": location_url},
        )


class UserTaskCompletionListByUser(generics.ListAPIView):
    serializer_class = UserTaskCompletionSerializer
    permission_classes = [HasAPIKeyPermission]

    def get_queryset(self):
        user = self.kwargs["user"]
        return UserTaskCompletion.objects.filter(user=user)


class UserTaskCompletionListByExercise(generics.ListAPIView):
    serializer_class = UserTaskCompletionSerializer
    permission_classes = [HasAPIKeyPermission]

    def get_queryset(self):
        exercise = self.kwargs["exercise"]
        return UserTaskCompletion.objects.filter(exercise=exercise)


class UserTaskCompletionListByCourse(generics.ListAPIView):
    serializer_class = UserTaskCompletionSerializer
    permission_classes = [HasAPIKeyPermission]

    def get_queryset(self):
        course = self.kwargs["course"]
        return UserTaskCompletion.objects.filter(instance=course)


class UserTaskCompletionListByUserCourse(generics.ListAPIView):
    serializer_class = UserTaskCompletionSerializer
    permission_classes = [HasAPIKeyPermission]

    def get_queryset(self):
        user = self.kwargs["user"]
        course = self.kwargs["course"]
        return UserTaskCompletion.objects.filter(user=user, instance=course)


class UserTaskCompletionRetrieveUpdateDestroy(
    MultipleFieldLookupMixin, generics.RetrieveUpdateDestroyAPIView
):
    queryset = UserTaskCompletion.objects.all()
    serializer_class = UserTaskCompletionSerializer
    permission_classes = [HasAPIKeyPermission]

    # 'instance' used instead of 'course' because it is the field
    # name in the model
    lookup_fields = ["user", "exercise", "instance"]
