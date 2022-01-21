from . import api
from django.urls import include, path
from rest_framework.authtoken import views

urlpatterns = [
    path("login/", views.obtain_auth_token),
    path("logout/", api.Logout.as_view()),
    path("register/", api.Registration.as_view()),
    path("user/", api.User.as_view()),
]
