from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """
    自定义用户模型
    区分：新生学生、系统管理员
    """
    # 用户角色选项
    ROLE_CHOICES = (
        ('student', '在校新生'),
        ('admin', '系统管理员'),
    )
    # 扩展用户字段
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student', verbose_name="用户角色")
    student_id = models.CharField(max_length=20, unique=True, blank=True, null=True, verbose_name="学号")
    phone = models.CharField(max_length=11, blank=True, null=True, verbose_name="手机号码")
    major = models.CharField(max_length=50, blank=True, null=True, verbose_name="所属专业")
    gender = models.CharField(max_length=5, blank=True, null=True, verbose_name="性别")

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        # 后台页面展示格式：学号-用户名
        return f"{self.student_id}-{self.username}" if self.student_id else self.username