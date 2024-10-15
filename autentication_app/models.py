from django.db import models
from django.contrib.auth.models import AbstractUser
from .validator import *

# Create your models here.

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=12, validators=[validate_only_phone],blank=True, null=True)
    picture = models.ImageField(upload_to='User/Picture', blank=True, null=True)
    dni = models.CharField(max_length=12, validators=[validate_only_dni], blank=True, null=True)

    
