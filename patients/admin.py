from django.contrib import admin
from .models import Patient

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ("cid", "hn", "first_name", "last_name", "phone", "created_at")
    search_fields = ("cid", "hn", "first_name", "last_name")
