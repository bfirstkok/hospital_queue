# patients/models.py
from django.db import models

class Patient(models.Model):
    GENDER_CHOICES = [
        ("M", "ชาย"),
        ("F", "หญิง"),
        ("O", "อื่นๆ"),
    ]

    BLOOD_CHOICES = [
        ("A", "A"), ("B", "B"), ("AB", "AB"), ("O", "O"),
        ("UNKNOWN", "ไม่ทราบ"),
    ]

    # เดิม
    first_name = models.CharField(max_length=100)
    last_name  = models.CharField(max_length=100)
    national_id = models.CharField(max_length=13, unique=True)

    # ✅ เพิ่ม: เพศ + อายุ + เบอร์โทร
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default="UNKNOWN")
    age = models.PositiveIntegerField(null=True, blank=True)
    phone = models.CharField(max_length=20, blank=True, default="")

    # ✅ medical record เต็ม (ทำเป็น optional เพื่อไม่บังคับกรอกทุกครั้ง)
    hn = models.CharField(max_length=20, blank=True, default="", db_index=True)

    address = models.TextField(blank=True, default="")

    blood_type = models.CharField(max_length=10, choices=BLOOD_CHOICES, default="UNKNOWN")

    height_cm = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    weight_kg = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    chronic_diseases = models.TextField(blank=True, default="")   # โรคประจำตัว
    allergies = models.TextField(blank=True, default="")          # แพ้ยา/อาหาร
    medications = models.TextField(blank=True, default="")        # ยาที่ใช้ประจำ
    emergency_name = models.CharField(max_length=120, blank=True, default="")
    emergency_phone = models.CharField(max_length=20, blank=True, default="")

    note = models.TextField(blank=True, default="")

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.national_id})"
