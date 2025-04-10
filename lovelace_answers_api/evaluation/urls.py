from django.urls import path
from . import views

urlpatterns = [
    path("evaluations/", views.EvaluationList.as_view(), name="get-evaluations"),
    path(
        "staff/<str:user>/evaluations/",
        views.EvaluationListByStaff.as_view(),
        name="get-evaluations-by-staff",
    ),
    path(
        "answers/<int:answer>/evaluation/",
        views.EvaluationRetrieveUpdateDestroy.as_view(),
        name="get-put-patch-delete-evaluation",
    ),
]
