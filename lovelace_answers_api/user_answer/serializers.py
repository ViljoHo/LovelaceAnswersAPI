from rest_framework import serializers
from .models import UserAnswer, UserTextfieldExerciseAnswer, UserMultipleChoiceExerciseAnswer


class UserTextfieldExerciseAnswerSerializer(serializers.ModelSerializer):
  class Meta:
    model = UserTextfieldExerciseAnswer
    exclude = ['polymorphic_ctype']


class UserMultipleChoiceExerciseAnswerSerializer(serializers.ModelSerializer):
    class Meta:
      model = UserMultipleChoiceExerciseAnswer
      exclude = ['polymorphic_ctype']


class BaseUserAnswerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserAnswer
        exclude = ['polymorphic_ctype']

class DynamicUserAnswerSerializer(serializers.Serializer):

    def to_representation(self, instance):
        if isinstance(instance, UserTextfieldExerciseAnswer):
            return UserTextfieldExerciseAnswerSerializer(instance).data
        elif isinstance(instance, UserMultipleChoiceExerciseAnswer):
            return UserMultipleChoiceExerciseAnswerSerializer(instance).data
        return BaseUserAnswerSerializer(instance).data