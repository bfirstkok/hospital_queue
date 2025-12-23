from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils import timezone
from queues.models import Queue

@login_required
def dashboard_view(request):
    waiting = Queue.objects.filter(status="WAITING")
    called = Queue.objects.filter(status="CALLED")

    context = {
        "waiting_total": waiting.count(),
        "called_total": called.count(),
        "red_total": waiting.filter(priority=1).count(),
        "yellow_total": waiting.filter(priority=2).count(),
        "green_total": waiting.filter(priority=3).count(),
        "now": timezone.now(),
    }
    return render(request, "dashboard/dashboard.html", context)
