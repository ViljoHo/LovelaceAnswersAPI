from django.urls import path

from . import views

urlpatterns = [
    path(
        "completions/",
        views.UserTaskCompletionListCreate.as_view(),
        name="get-post-completions",
    ),
    path(
        "users/<str:user>/completions/",
        views.UserTaskCompletionListByUser.as_view(),
        name="get-completions-by-user",
    ),
    path(
        "exercises/<str:exercise>/completions/",
        views.UserTaskCompletionListByExercise.as_view(),
        name="get-completions-by-exercise",
    ),
    path(
        "courses/<str:course>/completions/",
        views.UserTaskCompletionListByCourse.as_view(),
        name="get-completions-by-course",
    ),
    # path("users/<str:user>/exercises/<str:exercise>/completions/", views.UserTaskCompletionListByUserExercise.as_view(), name="completions-by-user-exercise"),
    path(
        "users/<str:user>/courses/<str:course>/completions/",
        views.UserTaskCompletionListByUserCourse.as_view(),
        name="get-completions-by-user-course",
    ),
    path(
        "users/<str:user>/exercises/<str:exercise>/courses/<str:instance>/completions/",
        views.UserTaskCompletionRetrieveUpdateDestroy.as_view(),
        name="get-put-patch-delete-completion",
    ),
]
