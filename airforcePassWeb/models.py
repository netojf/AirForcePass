from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class userProperties(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.TextField(max_length=11, unique=True)
    saram = models.TextField()
    birthDate = models.DateField()


class dependent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.TextField(max_length=120)
    email = models.EmailField()
    birthDate = models.DateField()
    cpf = models.TextField(max_length=11, unique=True)
