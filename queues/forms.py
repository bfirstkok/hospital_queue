from django import forms
from .models import VitalSign

class VitalSignForm(forms.ModelForm):
    class Meta:
        model = VitalSign
        fields = ["rr", "pr", "sys_bp", "dia_bp", "bt", "o2sat"]
