from django.contrib.auth.models import User
from django.db import models
from AirforcePass import settings

# Create your models here.
class userProperties(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userproperties', null=False, name='user')
    cpf = models.CharField(max_length=14, unique=True)
    saram = models.CharField(max_length=15)
    birthDate = models.DateField(blank=True, null=True)
    photo = models.ImageField(null=True, blank=True)


class dependent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.TextField(max_length=120)
    email = models.EmailField()
    birthDate = models.DateField(blank=True, null=True)
    cpf = models.CharField(max_length=14, unique=True)
