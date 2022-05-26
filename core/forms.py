from django import forms
from .models import Child

class ChildCreateForm(forms.ModelForm):
    class Meta:
        model = Child
        exclude = ['uuid', 'doctor']