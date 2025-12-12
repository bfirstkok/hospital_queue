from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ["cid", "hn", "first_name", "last_name", "phone", "birth_date"]
