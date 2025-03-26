from django.shortcuts import get_object_or_404, render
from rest_framework import generics
from .models import UserTaskCompletion
from .serializers import UserTaskCompletionSerializer


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

# class UserTaskCompletionListByUserExercise(generics.ListAPIView):
#     serializer_class = UserTaskCompletionSerializer

#     def get_queryset(self):
#         user = self.kwargs['user']
#         exercise = self.kwargs['exercise']
#         return UserTaskCompletion.objects.filter(user=user, exercise=exercise)

class UserTaskCompletionListByUserCourse(generics.ListAPIView):
    serializer_class = UserTaskCompletionSerializer

    def get_queryset(self):
        user = self.kwargs['user']
        course = self.kwargs['course']
        return UserTaskCompletion.objects.filter(user=user, instance=course)
    
class MultipleFieldLookupMixin:
    """
    FROM: https://www.django-rest-framework.org/api-guide/generic-views/#creating-custom-mixins

    Apply this mixin to any view or viewset to get multiple field filtering
    based on a `lookup_fields` attribute, instead of the default single field filtering.
    """
    def get_object(self):
        queryset = self.get_queryset()             # Get the base queryset
        queryset = self.filter_queryset(queryset)  # Apply any filter backends
        filter = {}
        for field in self.lookup_fields:
            if self.kwargs.get(field): # Ignore empty fields.
                filter[field] = self.kwargs[field]
        obj = get_object_or_404(queryset, **filter)  # Lookup the object
        self.check_object_permissions(self.request, obj)
        return obj

class UserTaskCompletionRetrieveUpdateDestroy(MultipleFieldLookupMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = UserTaskCompletion.objects.all()
    serializer_class = UserTaskCompletionSerializer
    lookup_fields = ['user', 'exercise', 'instance']
