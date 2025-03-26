from django.urls import path
from . import views

urlpatterns = [
    path("answers/", views.UserAnswerListView.as_view(), name="useranswer-view-list"),
    path("answers/textfield/", views.UserTextfieldExerciseAnswerCreateView.as_view(), name="textfieldanswer-view-create"),
    path("users/<str:user>/answers/", views.SpesificUserAnswerListView.as_view(), name="get-by-user"),
    path("exercises/<str:exercise>/answers/", views.SpesificExerciseAnswerListView.as_view(), name="get-by-exercise")
]