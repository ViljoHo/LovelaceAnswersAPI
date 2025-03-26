from django.db import models

# Create your models here.
class UserTaskCompletion(models.Model):
    class Meta:
        unique_together = ("exercise", "instance", "user")

    exercise = models.CharField(max_length=255)
    user = models.CharField(max_length=255)
    instance = models.CharField(max_length=255)
    points = models.DecimalField(default=0, max_digits=8, decimal_places=5)
    state = models.CharField(
        max_length=16,
        choices=(
            ("unanswered", "The task has not been answered yet"),
            ("correct", "The task has been answered correctly"),
            ("incorrect", "The task has not been answered correctly"),
            ("credited", "The task has been credited by completing another task"),
            ("submitted", "An answer has been submitted, awaiting assessment"),
            ("ongoing", "The task has been started"),
        ),
    )
