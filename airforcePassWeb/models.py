from django.contrib.auth.models import User
from django.db import models
from AirforcePass import settings

# Create your models here.
class userProperties(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.IntegerField( unique=True)
    saram = models.CharField(max_length=15)
    birthDate = models.DateField()
    photo = models.ImageField(null=True)


class dependent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.TextField(max_length=120)
    email = models.EmailField()
    birthDate = models.DateField()
    cpf = models.IntegerField( unique=True)
