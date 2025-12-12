from django.contrib import admin
from .models import Visit, VitalSign, Queue, TriageResult

admin.site.register(Visit)
admin.site.register(VitalSign)
admin.site.register(Queue)
admin.site.register(TriageResult)
