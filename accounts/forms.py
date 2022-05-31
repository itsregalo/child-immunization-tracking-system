from django import forms
from .models import *


class DoctorRegistrationForm(forms.ModelForm):
    class Meta:
        model = Doctor
        exclude = ['user', 'is_verified', 'profile_picture_thumbnail']
        widgets = {
            'license_no': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_no': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'speciality': forms.TextInput(attrs={'class': 'form-control'}),
            'about': forms.Textarea(attrs={'class': 'form-control'}),
            'profile_picture': forms.FileInput(attrs={'class': 'upload', 'rows': '5'}),
        }
