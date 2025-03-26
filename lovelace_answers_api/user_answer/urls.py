from django.urls import path
from . import views

urlpatterns = [
    path("answers/", views.AnswerList.as_view(), name="useranswer-view-list"),
    path("answers/textfield/", views.UserTextfieldExerciseAnswerCreate.as_view(), name="textfieldanswer-view-create"),
    path("users/<str:user>/answers/", views.AnswerListByUser.as_view(), name="get-by-user"),
    path("exercises/<str:exercise>/answers/", views.AnswerListByExercise.as_view(), name="get-by-exercise"),
    path("courses/<str:course>/answers/", views.AnswerListByCourse.as_view(), name="get-by-course"),
    path("users/<str:user>/exercises/<str:exercise>/answers/", views.AnswerListByUserAndExercise.as_view(), name="get-by-user-and-exercise"),
    path("users/<str:user>/courses/<str:course>/answers/", views.AnswerListByUserAndCourse.as_view(), name="get-by-user-and-course"),
    path("answers/<int:id>/", views.SpecificAnswer.as_view(), name="get-specific-answer")
]