from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class FitnessSession(models.Model):
    workout_type = models.TextField()
    workout_length = models.IntegerField()
    strength = models.IntegerField()
    created_by = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)



class User(models.Model):
    user_name = models.TextField()
    email = models.TextField()
    password = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)


