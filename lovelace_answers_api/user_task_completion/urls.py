from django.urls import path
from . import views

urlpatterns = [
    path("completions/", views.UserTaskCompletionListCreate.as_view(), name="completions-view-create"),
]