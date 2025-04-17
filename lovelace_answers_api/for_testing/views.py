from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from user_answer.models import UserAnswer
from evaluation.models import Evaluation
from user_task_completion.models import UserTaskCompletion
from api_keys.permissions import HasAPIKeyPermission


class ResetUserAnswersView(APIView):
    permission_classes = [HasAPIKeyPermission]

    def delete(self, request, format=None):

        UserAnswer.objects.all().delete()

        return Response(
            {"message": "All UserAnswers deleted."}, status=status.HTTP_204_NO_CONTENT
        )
    
class ResetEvaluationsView(APIView):
    permission_classes = [HasAPIKeyPermission]

    def delete(self, request, format=None):

        Evaluation.objects.all().delete()

        return Response(
            {"message": "All Evaluations deleted."}, status=status.HTTP_204_NO_CONTENT
        )
    
class ResetUserTaskCompletionsView(APIView):
    permission_classes = [HasAPIKeyPermission]

    def delete(self, request, format=None):

        UserTaskCompletion.objects.all().delete()

        return Response(
            {"message": "All UserTaskCompletions deleted."}, status=status.HTTP_204_NO_CONTENT
        )
