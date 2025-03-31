from django.db import models
from polymorphic.models import PolymorphicModel
from evaluation.models import Evaluation

# Create your models here.
class UserAnswer(PolymorphicModel):
    """
    Parent class for what users have given as their answers to different exercises.

    SET_NULL should be used as the on_delete behaviour for foreignkeys pointing to the
    exercises. The answers will then be kept even when the exercise is deleted.
    """
    
    exercise = models.CharField(max_length=255)
    instance = models.CharField(max_length=255) # CourseInstance reference
    user = models.CharField(max_length=255) # User reference
    evaluation = models.ForeignKey(Evaluation, null=True, blank=True, on_delete=models.SET_NULL)
    revision = models.PositiveIntegerField()  # The revision info is always required!
    language_code = models.CharField(max_length=7)
    answer_date = models.DateTimeField(
        verbose_name="Date and time of when the user answered this exercise", auto_now_add=True
    )
    answerer_ip = models.GenericIPAddressField()
    task_id = models.CharField(max_length=36, null=True, blank=True)

    collaborators = models.TextField(
        verbose_name="Which users was this exercise answered with", blank=True, null=True
    )
    checked = models.BooleanField(verbose_name="This answer has been checked", default=False)
    draft = models.BooleanField(verbose_name="This answer is a draft", default=False)

class UserTextfieldExerciseAnswer(UserAnswer):
    given_answer = models.TextField()


class UserMultipleChoiceExerciseAnswer(UserAnswer):
    chosen_answer = models.CharField(max_length=255)

class UserMultipleQuestionExamAnswer(UserAnswer):
    attempt = models.CharField(max_length=255)
    answers = models.JSONField()
