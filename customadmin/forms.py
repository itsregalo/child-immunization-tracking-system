from django import forms
from core.models import Vaccines

class VaccineForm(forms.ModelForm):
    class Meta:
        model = Vaccines
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'time_given': forms.TextInput(attrs={'class': 'form-control'}),
            'order': forms.NumberInput(attrs={'class': 'form-control'}),
        }