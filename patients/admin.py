# patients/admin.py
from django.contrib import admin
from .models import Patient

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "hn",
        "national_id",
        "first_name",
        "last_name",
        "gender",
        "age",
        "phone",
    )
    search_fields = ("hn", "national_id", "first_name", "last_name", "phone")
    list_filter = ("gender",)
