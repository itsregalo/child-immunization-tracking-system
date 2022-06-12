from django import forms
from .models import *
# import authenicate
from django.contrib.auth import authenticate, login


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

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    fields = ['username', 'password']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not username:
            raise forms.ValidationError('Username is required')
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not password:
            raise forms.ValidationError('Password is required')
        return password

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        if not username or not password:
            raise forms.ValidationError('Username and Password are required')
        return cleaned_data

    def save(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            return user
        else:
            raise forms.ValidationError('Invalid username or password')

class RegistrationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', max_length=100, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone_no = forms.CharField(label='Phone No', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    fields = ['username', 'email', 'phone_no', 'password', 'confirm_password']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not username:
            raise forms.ValidationError('Username is required')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError('Email is required')
        return email

    def clean_phone_no(self):
        phone_no = self.cleaned_data.get('phone_no')
        if not phone_no:
            raise forms.ValidationError('Phone No is required')
        return phone_no

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not password:
            raise forms.ValidationError('Password is required')
        return password

    def clean_confirm_password(self):
        confirm_password = self.cleaned_data.get('confirm_password')
        if not confirm_password:
            raise forms.ValidationError('Confirm Password is required')
        return confirm_password

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        phone_no = cleaned_data.get('phone_no')
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if not username or not email or not phone_no or not password or not confirm_password:
            raise forms.ValidationError('All fields are required')
        if password != confirm_password:
            raise forms.ValidationError('Passwords do not match')
        return cleaned_data

    def save(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        phone_no = self.cleaned_data.get('phone_no')
        password = self.cleaned_data.get('password')
        # check if user already exists
        user = User.objects.filter(username=username)
        if user:
            raise forms.ValidationError('Username already exists')
        user = User.objects.filter(email=email)
        if user:
            raise forms.ValidationError('Email already exists')
        user = User.objects.create_user(username=username,phone_no=phone_no, email=email, password=password)
        user.save()
        return user

