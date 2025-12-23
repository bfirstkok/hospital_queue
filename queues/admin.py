from django.contrib import admin
from .models import Visit, VitalSign, Queue, TriageResult,Device, TelemetryLog

admin.site.register(Visit)
admin.site.register(VitalSign)
admin.site.register(Queue)
admin.site.register(TriageResult)
admin.site.register(Device)
admin.site.register(TelemetryLog)
