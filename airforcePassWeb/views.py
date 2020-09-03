from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, reverse,get_object_or_404
from django import forms
import logging
logger = logging.getLogger('app_api') #from LOGGING.loggers in settings.py
from .forms import userForm, userPropForm

def index(request):
    userform = userForm()
    propform = userPropForm()
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('airforcePassWeb:signIn'))

    users = User.objects.all()
    return render(request, 'users/index.html', {
        'users': users,
        'userform' : userform,
        'propertyform' : propform
    })


def userSignIn(request):
    userform = userForm()
    propform = userPropForm()
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST["username"]
            password = request.POST["password"]

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'users/userSignIn.html', {
                    "message" : "logged",
                    'userform' : userform,
                    'propertyform' : propform,
                    'user' : user
                })
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
    else:
        return render(request, 'users/userSignIn.html', {
                    "message" : "logged",
                    'userform' : userform,
                    'propertyform' : propform,
                    'user' : request.user})
    
    


def logout_view(request):
    logout(request)
    return HttpResponseRedirect( str(request.META.get('HTTP_REFERER')), {
                "message": "Logged Out"
            })


def userSignUp(request, currentmessage = ''):
    if request.method == 'POST':
        userform = userForm(request.POST)
        userprop = userPropForm(request.POST, request.FILES)
    
        if userform.is_valid() and userprop.is_valid():
            
            userform.save(commit=True)
            newuser = get_object_or_404(User, username=userform.cleaned_data['username'])
            userprop.save(newuser,commit=True)

            if not request.user.is_authenticated:
                print(userform.cleaned_data['password1'])

                user1 = authenticate(username=userform.cleaned_data['username'], password=userform.cleaned_data['password1'])
                print(user1)
                if user1:
                    if user1.is_active:
                        login(request, user1)
                        return render(request, 'users/userSignIn.html', {
                        "message" : "logged",
                        'userform' : userform,
                        'propertyform' : userprop,
                        'user' : user1
                    })
                else:
                    return render(request, 'users/userSignIn.html', {
                        "message" : "blocked",
                        'userform' : userform,
                        'propertyform' : userprop
                    })
            return render(request, 'users/userSignIn.html', {
                "message" : "logged",
                'userform' : userform,
                'propertyform' : userprop
            })
        else:
            return render(request, 'users/userSignIn.html',{
                "userform" : userform,
                'propertyform' : userprop,
                'message' : 'blocked'})

    # else:
    #     userform = userForm()
    #     propform = userPropForm()
    #     if (not propform):
    #         print ("nulo aqui tbm")
    #     else:   
    #         print ('alguma coisa ta errada')
    #     return render(request, 'users/userSignIn.html',{
    #         "userform" : userform,
    #         'propertyform' : propform
    # })




