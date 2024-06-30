from django import forms

from .models import Measurements


class MeasurementForm(forms.ModelForm):
    class Meta:
        model = Measurements
        fields =[
            'height',
            'weight',
            'biceps',
            'forearm',
            'shoulder',
            'chest',
            'waist',
            'thighs',
            'calf',
            'measured_date'
        ]
        widgets = {
            'height': forms.NumberInput(attrs={'class': 'form-control'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control'}),
            'biceps': forms.NumberInput(attrs={'class': 'form-control'}),
            'forearm': forms.NumberInput(attrs={'class': 'form-control'}),
            'shoulder': forms.NumberInput(attrs={'class': 'form-control'}),
            'chest': forms.NumberInput(attrs={'class': 'form-control'}),
            'waist': forms.NumberInput(attrs={'class': 'form-control'}),
            'thighs': forms.NumberInput(attrs={'class': 'form-control'}),
            'calf': forms.NumberInput(attrs={'class': 'form-control'}),
            'measured_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

        