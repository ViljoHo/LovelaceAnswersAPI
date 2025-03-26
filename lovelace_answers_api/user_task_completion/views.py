from rest_framework import generics
from .models import UserTaskCompletion
from .serializers import UserTaskCompletionSerializer

from .utils import MultipleFieldLookupMixin


class UserTaskCompletionListCreate(generics.ListCreateAPIView):
    queryset = UserTaskCompletion.objects.all()
    serializer_class = UserTaskCompletionSerializer

class UserTaskCompletionListByUser(generics.ListAPIView):
    serializer_class = UserTaskCompletionSerializer

    def get_queryset(self):
        user = self.kwargs['user']
        return UserTaskCompletion.objects.filter(user=user)
    
class UserTaskCompletionListByExercise(generics.ListAPIView):
    serializer_class = UserTaskCompletionSerializer

    def get_queryset(self):
        exercise = self.kwargs['exercise']
        return UserTaskCompletion.objects.filter(exercise=exercise)
    
class UserTaskCompletionListByCourse(generics.ListAPIView):
    serializer_class = UserTaskCompletionSerializer

    def get_queryset(self):
        course = self.kwargs['course']
        return UserTaskCompletion.objects.filter(instance=course)

class UserTaskCompletionListByUserCourse(generics.ListAPIView):
    serializer_class = UserTaskCompletionSerializer

    def get_queryset(self):
        user = self.kwargs['user']
        course = self.kwargs['course']
        return UserTaskCompletion.objects.filter(user=user, instance=course)

class UserTaskCompletionRetrieveUpdateDestroy(MultipleFieldLookupMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = UserTaskCompletion.objects.all()
    serializer_class = UserTaskCompletionSerializer
    lookup_fields = ['user', 'exercise', 'instance']
