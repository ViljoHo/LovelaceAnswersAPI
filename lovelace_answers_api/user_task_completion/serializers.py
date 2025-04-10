from rest_framework import serializers

from .models import UserTaskCompletion


class UserTaskCompletionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTaskCompletion
        exclude = ["id"]
