from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import userProperties, dependent
from django import forms
from django.forms import ModelForm
from AirforcePass import settings


class userForm(ModelForm):

    error_messages = {
        'password_mismatch': "As duas senhas devem coincidir",
    }
    username = forms.CharField(label="Usuário", help_text="")
    first_name = forms.CharField(label="Nome")
    last_name = forms.CharField(label="Sobrenome")
    password1 = forms.CharField(label="Senha",
        widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmação da Senha",
        widget=forms.PasswordInput)
    email = forms.EmailField( required=True)

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

    # def is_valid(self):
    #     return True

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
         widget=forms.DateInput(attrs={'type':'date'} , format = '%d/%m/%Y'))

    photo = forms.ImageField(
        label="Foto", 
        required=False)

    cpf = forms.CharField(max_length=14 ,widget=forms.TextInput( attrs={'data-mask':"000.000.000.00",}))

    class Meta:
        model = userProperties
        exclude = ['user']

    # def is_valid(self):
    #     return True

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