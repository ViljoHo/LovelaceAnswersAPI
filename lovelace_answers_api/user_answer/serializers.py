from rest_framework import serializers
from .models import UserAnswer, UserTextfieldExerciseAnswer, UserMultipleChoiceExerciseAnswer


class UserTextfieldExerciseAnswerSerializer(serializers.ModelSerializer):
  class Meta:
    model = UserTextfieldExerciseAnswer
    fields = '__all__'


class UserMultipleChoiceExerciseAnswerSerializer(serializers.ModelSerializer):
    class Meta:
      model = UserMultipleChoiceExerciseAnswer
      fields = '__all__'


class BaseUserAnswerSerializer(serializers.ModelSerializer):
    """Perusserialisoija kaikille muille UserAnswer-tyypeille"""
    class Meta:
        model = UserAnswer
        fields = '__all__'

class DynamicUserAnswerSerializer(serializers.Serializer):
    """Dynaaminen serialisoija, joka valitsee oikean serialisoijan"""

    def to_representation(self, instance):
        if isinstance(instance, UserTextfieldExerciseAnswer):
            return UserTextfieldExerciseAnswerSerializer(instance).data
        elif isinstance(instance, UserMultipleChoiceExerciseAnswer):
            return UserMultipleChoiceExerciseAnswerSerializer(instance).data
        return BaseUserAnswerSerializer(instance).data