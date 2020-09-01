from django.urls import path

from . import views

app_name = "airforcePassWeb"

urlpatterns = [
    path("signin/", views.userSignIn, name="userSignIn"),
    path('index/', views.index, name='index'),
    path('', views.userLogin, name='login'),
    path('signUp', views.userSignUp, name='signUp')
]
