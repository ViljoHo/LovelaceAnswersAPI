from django.db import models
from polymorphic.models import PolymorphicModel

# Create your models here.
class UserAnswer(PolymorphicModel):
    """
    Parent class for what users have given as their answers to different exercises.

    SET_NULL should be used as the on_delete behaviour for foreignkeys pointing to the
    exercises. The answers will then be kept even when the exercise is deleted.
    """

    #html_extra_class = ""
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

    # NOTE: This should be obsolete and replaced by content page's get_user_answers
    @staticmethod
    def get_task_answers(task, instance=None, user=None, revision=None):
        if task.content_type == "CHECKBOX_EXERCISE":
            answers = UserAnswer.objects.filter(usercheckboxexerciseanswer__exercise=task)
        elif task.content_type == "MULTIPLE_CHOICE_EXERCISE":
            answers = UserAnswer.objects.filter(usermultiplechoiceexerciseanswer__exercise=task)
        elif task.content_type == "TEXTFIELD_EXERCISE":
            answers = UserAnswer.objects.filter(usertextfieldexerciseanswer__exercise=task)
        elif task.content_type == "FILE_UPLOAD_EXERCISE":
            answers = UserAnswer.objects.filter(userfileuploadexerciseanswer__exercise=task)
        elif task.content_type == "REPEATED_TEMPLATE_EXERCISE":
            answers = UserAnswer.objects.filter(userrepeatedtemplateexerciseanswer__exercise=task)
        else:
            raise ValueError(f"Task {task} does not have a valid exercise type")

        if instance:
            answers = answers.filter(instance=instance)

        if user:
            answers = answers.filter(user=user)

        if revision:
            answers = answers.filter(revision=revision)

        return answers.order_by("answer_date")
