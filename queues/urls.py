from django.urls import path
from . import views

urlpatterns = [
    path("", views.queue_list, name="queue_list"),
    path("call/<int:visit_id>/", views.call_visit, name="call_visit"),
    path("triage/<int:visit_id>/", views.triage_visit, name="triage_visit"),

]
