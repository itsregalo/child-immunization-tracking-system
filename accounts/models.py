from distutils.command.upload import upload
from email.policy import default
from tokenize import blank_re
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# imagekit
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


User = settings.AUTH_USER_MODEL
# Create your models here.

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female','Female'),
    ('Other', 'Other')
)

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
    gender = models.CharField(choices=GENDER_CHOICES, max_length=20)
    profile_picture = models.ImageField(upload_to='images/doctors_profile/%Y/%m', 
                                        default='images/default-avatar.jpg',
                                        blank=True, null=True)
    profile_picture_thumbnail = ImageSpecField(source='profile_picture',
                                            processors=[ResizeToFill(100, 100)],
                                            format='JPEG',
                                            options={'quality': 60}
                                                )
    about = models.TextField(blank=True, null=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class Parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254, blank=True, null=True)
    phone_no = models.CharField(max_length=13, blank=True, null=True)
    address = models.CharField(max_length=254, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='images/parents_profile/%Y/%m',
                                                    default='images/default-avatar.jpg',
                                                    blank=True, null=True)
    profile_picture_thumbnail = ImageSpecField(source='profile_picture',
                                            processors=[ResizeToFill(100, 100)],
                                            format='JPEG',
                                            options={'quality': 60}
                                                )

    def __str__(self):
        return self.user.username