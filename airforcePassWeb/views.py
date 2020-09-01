from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django import forms

# Create your views here.
from django.urls import reverse

class userForm(forms.Form):
    name = forms.CharField(label="Nome")
    cpf = forms.NumberInput()
    saram = forms.CharField(label='Saram')
    email = forms.EmailField(label='E-mail')
    confirmEmail = forms.EmailField(label='Confirmação de e-mail')
    birthDate = forms.DateField()


def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('airforcePassWeb:login'))

    users = User.objects.all()
    return render(request, 'users/index.html', {
        'users': users
    })


def userLogin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        usuario = authenticate(request, username=username, password=password)
        if usuario:
            login(request, user=usuario)
            return redirect('users/index')
        else:
            form_login = AuthenticationForm()
    else:
        form_login = AuthenticationForm()
    return render(request, 'users/login.html', {'form_login': form_login})


def userSignIn(request):
    if request.method == "POST":
        form_usuario = UserCreationForm(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('index')
    else:
        form_usuario = UserCreationForm()
    return render(request, 'users/userSignIn.html', {
        'form_usuario': form_usuario
    })

def userSignUp(request):
    if request.method == 'POST':
        form1 = userForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form1.save()
            return HttpResponseRedirect('Cadastrado com sucesso!')
        else:
            return HttpResponseRedirect('Usuário Inválido!')

    # if a GET (or any other method) we'll create a blank form
    else:
        form1 = userForm()
        return render(request, 'users/index.html',{
            "form1" : form1
    })

