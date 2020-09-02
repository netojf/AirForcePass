from django.urls import path

from . import views

app_name = "airforcePassWeb"

urlpatterns = [
    path("signin/", views.userSignIn, name="signIn"),
    path('', views.index, name='index'),
    path('signUp/', views.userSignUp, name='signUp'),
    path("logout", views.logout_view, name="logout")
]
