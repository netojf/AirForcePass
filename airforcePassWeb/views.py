from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, reverse,get_object_or_404
from django import forms
import logging
from .forms import userForm, userPropForm

logger = logging.getLogger('app_api') #from LOGGING.loggers in settings.py

 #index control to user logged page
def index(request):

    #check if user is logged 
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('airforcePassWeb:signIn'))


def userSignIn(request):
    
    userform = userForm()
    propform = userPropForm()
    
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST["username"]
            password = request.POST["password"]

            user = authenticate(username=username, password=password)
            #if authentication was sucessful
            if user is not None:
                if user.is_active:
                    login(request, user)

                    return render(request, 'users/userSignIn.html', {
                    "message" : "logged",
                    'userform' : userform,
                    'propertyform' : propform,
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
    

def user_update(request):
    if request.user.is_authenticated:
        userform = userForm(request or None, instance = request.user)
        userpropform = userPropForm(request or None, instance = request.user.userproperties)
    else:
        return render(request, 'users/userSignIn.html',{
                "userform" : userform,
                'propertyform' : userpropform,
                'message' : 'blocked'})
    if request.method == 'POST':
        if userform.is_valid() and userpropform.is_valid():
            userform.save(commit=True)
            newuser = get_object_or_404(User, username=userform.cleaned_data['username'])
            # ↓ pass the user to form to make the relationship ↓
            userpropform.save(newuser,commit=True)
            return render(request, 'users/userSignIn.html', {
                        "message" : "logged",
                        'userform' : userform,
                        'propertyform' : userpropform})
        else:
            # if the form is not valid return the page with modal opened 
            return render(request, 'users/userSignIn.html',{
                "userform" : userform,
                'propertyform' : userpropform,
                'message' : 'blocked',
                # ↓ open the modal ↓
                'modalMessage' : True})




def logout_view(request):
    logout(request)
    return HttpResponseRedirect( str(request.META.get('HTTP_REFERER')), {
                "message": "Logged Out"
            })

# user register control
def userSignUp(request, currentmessage = ''):
    if request.method == 'POST':
        userform = userForm(request.POST)
        userprop = userPropForm(request.POST, request.FILES)

        # check form validation
        if userform.is_valid() and userprop.is_valid():
            
            userform.save(commit=True)
            newuser = get_object_or_404(User, username=userform.cleaned_data['username'])
            # ↓ pass the user to form to make the relationship ↓
            userprop.save(newuser,commit=True)

            # login the new user ↓
            if not request.user.is_authenticated:
                user1 = authenticate(username=userform.cleaned_data['username'], password=userform.cleaned_data['password1'])
                
                if user1:
                    if user1.is_active:
                        login(request, user1)
                        return render(request, 'users/userSignIn.html', {
                        "message" : "logged",
                        'userform' : userform,
                        'propertyform' : userprop
                    })
                else:
                    # return the page to the user with the modal opened
                    return render(request, 'users/userSignIn.html', {
                        # ↓ change the image ↓
                        "message" : "blocked",
                        'userform' : userform,
                        'propertyform' : userprop,
                        
                    })
            # if the user is logged return a default login page ( just for exception handling)
            return render(request, 'users/userSignIn.html', {
                "message" : "logged",
                'userform' : userform,
                'propertyform' : userprop
            })
        else:
            # if the form is not valid return the page with modal opened 
            return render(request, 'users/userSignIn.html',{
                "userform" : userform,
                'propertyform' : userprop,
                'message' : 'blocked',
                # ↓ open the modal ↓
                'modalMessage' : True})




