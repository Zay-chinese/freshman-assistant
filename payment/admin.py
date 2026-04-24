from django.contrib import admin
from .models import PaymentRecord

@admin.register(PaymentRecord)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("student", "total_money", "status", "pay_time")
    list_filter = ("status",)
    search_fields = ("student__student_id",)