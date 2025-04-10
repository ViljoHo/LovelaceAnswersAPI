from rest_framework import serializers
from .models import (
    UserAnswer,
    UserCheckboxExerciseAnswer,
    UserTextfieldExerciseAnswer,
    UserMultipleChoiceExerciseAnswer,
    UserMultipleQuestionExamAnswer,
)
from evaluation.serializers import EvaluationSerializer


class BaseEvaluationControlSerializer(serializers.ModelSerializer):
    evaluation = serializers.SerializerMethodField()

    def get_evaluation(self, obj):
        request = self.context.get("request")
        if (
            request
            and request.parser_context
            and "id" in request.parser_context["kwargs"]
        ):
            return EvaluationSerializer(obj.evaluation).data if obj.evaluation else None

        return obj.evaluation.id if obj.evaluation else None


class UserTextfieldExerciseAnswerSerializer(BaseEvaluationControlSerializer):
    class Meta:
        model = UserTextfieldExerciseAnswer
        exclude = ["polymorphic_ctype"]


class UserMultipleChoiceExerciseAnswerSerializer(BaseEvaluationControlSerializer):
    class Meta:
        model = UserMultipleChoiceExerciseAnswer
        exclude = ["polymorphic_ctype"]


class UserMultipleQuestionExamAnswerSerializer(BaseEvaluationControlSerializer):
    class Meta:
        model = UserMultipleQuestionExamAnswer
        exclude = ["polymorphic_ctype"]


class UserCheckboxExerciseAnswerSerializer(BaseEvaluationControlSerializer):
    class Meta:
        model = UserCheckboxExerciseAnswer
        exclude = ["polymorphic_ctype"]


class BaseUserAnswerSerializer(BaseEvaluationControlSerializer):
    class Meta:
        model = UserAnswer
        exclude = ["polymorphic_ctype"]


class DynamicUserAnswerSerializer(serializers.Serializer):

    def to_representation(self, instance):
        context = self.context
        if isinstance(instance, UserTextfieldExerciseAnswer):
            return UserTextfieldExerciseAnswerSerializer(instance, context=context).data
        elif isinstance(instance, UserMultipleChoiceExerciseAnswer):
            return UserMultipleChoiceExerciseAnswerSerializer(
                instance, context=context
            ).data
        elif isinstance(instance, UserMultipleQuestionExamAnswer):
            return UserMultipleQuestionExamAnswerSerializer(
                instance, context=context
            ).data
        elif isinstance(instance, UserCheckboxExerciseAnswer):
            return UserCheckboxExerciseAnswerSerializer(instance, context=context).data
        return BaseUserAnswerSerializer(instance, context=context).data
