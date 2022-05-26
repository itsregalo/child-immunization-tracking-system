from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

User = settings.AUTH_USER_MODEL
# Create your models here.

class User(AbstractUser):
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    is_parent = models.BooleanField(default=True)
    is_ministry = models.BooleanField(default=False)
    phone_no = models.CharField(max_length=13, blank=True, null=True)
    ver_code = models.CharField(blank=True, null=True, max_length=10)

    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['username',]

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    license_no = models.CharField(max_length=20)
    email = models.EmailField(max_length=254, blank=True, null=True)
    phone_no = models.CharField(max_length=13, blank=True, null=True)
    address = models.CharField(max_length=254, blank=True, null=True)
    speciality = models.CharField(max_length=254, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='images/doctors_profile/%Y/%m', blank=True, null=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class Parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254, blank=True, null=True)
    phone_no = models.CharField(max_length=13, blank=True, null=True)
    address = models.CharField(max_length=254, blank=True, null=True)

    def __str__(self):
        return self.user.username