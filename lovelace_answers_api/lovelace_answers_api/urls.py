"""
URL configuration for lovelace_answers_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from environs import Env


env = Env()
env.read_env()

schema_view = get_schema_view(
    openapi.Info(
        title="Lovelace Answers API",
        default_version='v1',
        description="",
    ),
    public=True,
    permission_classes=(AllowAny,),
)


urlpatterns = [
    path('api/', include("user_answer.urls")),
    path('api/', include("evaluation.urls")),
    path('api/', include("user_task_completion.urls")),
]


if env.bool("TESTING"):
    env = Env()
    env.read_env()

    schema_view = get_schema_view(
        openapi.Info(
            title="Lovelace Answers API",
            default_version='v1',
            description="",
        ),
        public=True,
        permission_classes=(AllowAny,),
    )

    urlpatterns += [
        path('testing/', include("for_testing.urls")),
        path(
            'swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'
        ),
    ]
