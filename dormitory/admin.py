from django.contrib import admin
from .models import Dormitory

@admin.register(Dormitory)
class DormAdmin(admin.ModelAdmin):
    list_display = ("building", "room_num", "total_bed", "remain_bed")
    search_fields = ("building", "room_num")