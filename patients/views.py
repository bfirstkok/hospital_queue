from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import PatientForm
from .models import Patient
from queues.models import Visit, Queue
from queues.forms import VitalSignForm
from ai_triage.services import apply_ai_triage


def severity_to_priority(sev: str) -> int:
    # priority เลขน้อยมาก่อน
    return {"RED": 1, "YELLOW": 2, "GREEN": 3}.get(sev, 3)

@login_required
def register_patient(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name", "").strip()
        last_name = request.POST.get("last_name", "").strip()
        national_id = request.POST.get("national_id", "").strip()

        if first_name and last_name and national_id:
            Patient.objects.create(
                first_name=first_name,
                last_name=last_name,
                national_id=national_id,  # ถ้าฟิลด์จริงไม่ชื่อ national_id ให้เปลี่ยนตรงนี้
            )
            return redirect("queue_list")  # กลับหน้าคิว

    return render(request, "patients/register.html")
