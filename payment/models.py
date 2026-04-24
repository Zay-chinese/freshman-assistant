from django.db import models
from users.models import User

class PaymentRecord(models.Model):
    """
    新生缴费记录模型
    学费、住宿费缴费状态管理
    """
    PAY_STATUS = (
        ("unpaid", "未缴费"),
        ("paid", "已缴费"),
    )
    student = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="缴费新生")
    total_money = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="缴费总金额")
    pay_time = models.DateTimeField(null=True, blank=True, verbose_name="缴费时间")
    status = models.CharField(max_length=10, choices=PAY_STATUS, default="unpaid", verbose_name="缴费状态")

    class Meta:
        verbose_name = "缴费记录"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.student.student_id} - {self.get_status_display()}"