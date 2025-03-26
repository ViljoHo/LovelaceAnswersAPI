from django.db import models

# Create your models here.

class Evaluation(models.Model):
    """Evaluation of a student's answer to an exercise."""

    correct = models.BooleanField(default=False)
    suspect = models.BooleanField(default=False)
    points = models.DecimalField(default=0, max_digits=5, decimal_places=2)

    # max_points is separate from the task's default_points to allow
    # for flexibility in changing the point values of tasks.
    max_points = models.IntegerField(default=1)

    # Note: Evaluation should not be translated. The teacher should know which
    # language the student used and give an evaluation using that language.

    evaluation_date = models.DateTimeField(
        verbose_name="When was the answer evaluated", auto_now_add=True
    )
    evaluator = models.CharField(max_length=255)
    feedback = models.TextField(verbose_name="Feedback given by a teacher", blank=True)
    test_results = models.TextField(
        verbose_name="Test results in JSON", blank=True
    )  # TODO: JSONField
    comment = models.TextField(
        verbose_name="Comment about the evaluation for course staff only", blank=True
    )
