from django.contrib import admin
from .models import CheckInRecord

@admin.register(CheckInRecord)
class CheckInAdmin(admin.ModelAdmin):
    list_display = ("student", "dorm", "status", "checkin_time")
    list_filter = ("status",)
    search_fields = ("student__student_id",)