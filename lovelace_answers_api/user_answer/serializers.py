from rest_framework import serializers
from .models import (
    UserAnswer,
    UserCheckboxExerciseAnswer,
    UserTextfieldExerciseAnswer,
    UserMultipleChoiceExerciseAnswer,
    UserMultipleQuestionExamAnswer,
)
from evaluation.serializers import EvaluationSerializer


class UserTextfieldExerciseAnswerSerializer(serializers.ModelSerializer):
    # evaluation = EvaluationSerializer(read_only=True)

    class Meta:
        model = UserTextfieldExerciseAnswer
        exclude = ["polymorphic_ctype"]


class UserMultipleChoiceExerciseAnswerSerializer(serializers.ModelSerializer):
    # evaluation = EvaluationSerializer(read_only=True)

    class Meta:
        model = UserMultipleChoiceExerciseAnswer
        exclude = ["polymorphic_ctype"]


class UserMultipleQuestionExamAnswerSerializer(serializers.ModelSerializer):
    # evaluation = EvaluationSerializer(read_only=True)

    class Meta:
        model = UserMultipleQuestionExamAnswer
        exclude = ["polymorphic_ctype"]


class UserCheckboxExerciseAnswerSerializer(serializers.ModelSerializer):
    # evaluation = EvaluationSerializer(read_only=True)

    class Meta:
        model = UserCheckboxExerciseAnswer
        exclude = ["polymorphic_ctype"]


class BaseUserAnswerSerializer(serializers.ModelSerializer):
    # evaluation = EvaluationSerializer(read_only=True)

    class Meta:
        model = UserAnswer
        exclude = ["polymorphic_ctype"]


class DynamicUserAnswerSerializer(serializers.Serializer):

    def to_representation(self, instance):
        if isinstance(instance, UserTextfieldExerciseAnswer):
            return UserTextfieldExerciseAnswerSerializer(instance).data
        elif isinstance(instance, UserMultipleChoiceExerciseAnswer):
            return UserMultipleChoiceExerciseAnswerSerializer(instance).data
        elif isinstance(instance, UserMultipleQuestionExamAnswer):
            return UserMultipleQuestionExamAnswerSerializer(instance).data
        elif isinstance(instance, UserCheckboxExerciseAnswer):
            return UserCheckboxExerciseAnswerSerializer(instance).data
        return BaseUserAnswerSerializer(instance).data
