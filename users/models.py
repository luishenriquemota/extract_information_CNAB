from enum import unique
from wsgiref.validate import validator
from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid


class User(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    username = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=125, unique=True, blank=False)
    cpf = models.CharField(max_length=11, unique=True)

