from django.urls import path
from . import views

urlpatterns = [
    path("answers/", views.UserAnswerList.as_view(), name="useranswer-view-list"),
]