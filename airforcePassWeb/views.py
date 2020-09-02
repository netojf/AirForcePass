from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, reverse
from django import forms
import logging
logger = logging.getLogger('app_api') #from LOGGING.loggers in settings.py
from .forms import userForm, userPropForm


def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('airforcePassWeb:signIn'))

    users = User.objects.all()
    return render(request, 'users/index.html', {
        'users': users
    })


def userSignIn(request):
    userform = userForm()
    propform = userPropForm()
    if not request.user.is_authenticated:
        if request.method == 'POST':
            logger.info(request.POST["username"])
            
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse("airforcePassWeb:index"))
            else:
                return render(request, 'users/userSignIn.html', {
                    "message" : "blocked",
                    'userform' : userform,
                    'propertyform' : propform
                })
        return render(request, 'users/userSignIn.html', {
                    "message" : "login",
                    'userform' : userform,
                    'propertyform' : propform
                })
    
    return HttpResponseRedirect(reverse('airforcePassWeb:index'))


def logout_view(request):
    logout(request)
    return HttpResponseRedirect( str(request.META.get('HTTP_REFERER')), {
                "message": "Logged Out"
            })


def userSignUp(request):
    if request.method == 'POST':
        print('postsignup')
        userform = userForm(request.POST)
        if userform.is_valid():
            userform.save()
            return HttpResponseRedirect('Cadastrado com sucesso!')
        else:
            return HttpResponseRedirect('Usuário Inválido!')

    else:
        userform = userForm()
        propform = userPropForm()
        if (not propform):
            print ("nulo aqui tbm")
        else:   
            print ('alguma coisa ta errada')
        return render(request, 'users/userSignUp.html',{
            "userform" : userform,
            'propertyform' : propform
    })




