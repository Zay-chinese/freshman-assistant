from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # 后台表格展示字段
    list_display = ("username", "role", "student_id", "phone", "major")
    # 侧边筛选栏
    list_filter = ("role", "major")
    # 顶部搜索框
    search_fields = ("username", "student_id")