from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import userProperties, dependent
from django import forms
from django.forms import ModelForm
from AirforcePass import settings
from django.forms.utils import ErrorList


class DangerTextClass(ErrorList):
    def __str__(self):
        return self.as_custom

    def as_custom(self):
        if not self: return ''
        return '<div class="errorlist">%s</div>' % ''.join(['<div class="text-danger">%s</div>' % e for e in self])

class userForm(ModelForm):

    error_messages = {
        'password_mismatch': "As duas senhas devem coincidir",
        'username_exists' : "Usuário já existe"
    }
    error_class = DangerTextClass

    username = forms.CharField(label="Usuário", error_messages={}, help_text="", 
    widget=forms.TextInput(attrs={'class': 'form-control'}))

    first_name = forms.CharField(label="Nome", 
    widget=forms.TextInput(attrs={'class': 'form-control'}))

    last_name = forms.CharField(label="Sobrenome", 
    widget=forms.TextInput(attrs={'class': 'form-control'}))

    password1 = forms.CharField(label="Senha",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    password2 = forms.CharField(label="Confirmação da Senha",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    email = forms.EmailField( required=True,
     widget= forms.EmailInput(attrs={'class': 'form-control'}))


    class Meta:
        model = User
        fields = ("username","first_name",
        "last_name",
        "email")

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2


    def clean_username(self):
        username = self.cleaned_data.get("username")

        try:
            User._default_manager.get(username=username)
            #if the user exists, then let's raise an error message

            raise forms.ValidationError( 
            self.error_messages['username_exists'],  #my error message

            code='username_exists',   #set the error message key

                )
        except User.DoesNotExist:
            return username # if user does not exist so we can continue the registration process


    def save(self, commit=True):
        user = super(userForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        

        if commit:
            user.save()
        return user
    
    

class userPropForm(forms.ModelForm):
    birthDate = forms.DateField(
        label = "Data de Aniversário",
         required=False,
         widget=forms.DateInput(attrs={'type':'date','class':'form-control'} , format = '%d/%m/%Y'))

    photo = forms.ImageField(
        label="Foto", 
        required=False, widget=forms.FileInput(attrs={'class':'form-control-file'}))

    cpf = forms.CharField(max_length=14 ,widget=forms.TextInput( attrs={'class':'form-control','data-mask':"000.000.000.00",}))

    saram = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = userProperties
        exclude = ['user']

    def save(self,user, commit=True):
        userprop = super(userPropForm, self).save(commit=False)
        userprop.cpf = (self.cleaned_data["cpf"])
        userprop.saram = self.cleaned_data['saram']
        userprop.birthdate = self.cleaned_data['birthDate']
        userprop.photo = self.cleaned_data['photo']
        userprop.user = user
        if commit:
            userprop.save()
        return userprop