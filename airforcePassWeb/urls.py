from django.urls import path

from . import views

app_name = "airforcePassWeb"

urlpatterns = [
    path("", views.userSigIn, name="userSignIn"),
]
