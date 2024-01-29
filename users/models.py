from django.db import models
from django.contrib.auth.models import AbstractUser
from books.models import GenderModel

class UserModel(AbstractUser):
    gender = models.CharField(max_length=10, choices=GenderModel.GENDER_CHOICES, blank=True)
    user_image = models.ImageField(upload_to='user_images', blank=True, null=True)
    passport_id = models.CharField(max_length=9, blank=True, null=True)
    birthday = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=13, null=True, blank=True)
    address = models.CharField(max_length=225, null=True, blank=True)
    work_address = models.CharField(max_length=225, null=True, blank=True)
    profile_id = models.CharField(max_length=100, null=True)
    profile_ball = models.IntegerField(default=0, blank=True)
    profile_balance = models.FloatField(default=0, blank=True)
