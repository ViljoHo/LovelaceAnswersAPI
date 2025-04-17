from django.urls import path
from . import views

urlpatterns = [
    path("reset/answers/", views.ResetUserAnswersView.as_view(), name="reset-answers"),
    path("reset/evaluations/", views.ResetEvaluationsView.as_view(), name="reset-evaluations"),
    path("reset/completions/", views.ResetUserTaskCompletionsView.as_view(), name="reset-completions")
]