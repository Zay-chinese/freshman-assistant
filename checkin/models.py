from django.db import models
from users.models import User
from dormitory.models import Dormitory

class CheckInRecord(models.Model):
    """
    新生报到记录模型（项目核心业务表）
    预报到、报到状态、宿舍分配全部存在这张表
    """
    STATUS_CHOICES = (
        ("pending", "待报到"),
        ("completed", "已完成报到"),
        ("cancel", "报到驳回"),
    )
    # 关联新生用户（一个新生仅一条报到记录）
    student = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="新生用户")
    # 关联分配的宿舍
    dorm = models.ForeignKey(Dormitory, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="分配宿舍")
    # 报到信息字段
    checkin_time = models.DateTimeField(null=True, blank=True, verbose_name="实际报到时间")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending", verbose_name="报到状态")
    remark = models.TextField(blank=True, null=True, verbose_name="管理员备注")

    class Meta:
        verbose_name = "新生报到记录"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.student.student_id} - {self.get_status_display()}"
