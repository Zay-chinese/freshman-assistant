from django.db import models

class Dormitory(models.Model):
    """
    宿舍信息模型
    宿舍、楼栋、床位管理
    """
    building = models.CharField(max_length=10, verbose_name="楼栋号")
    room_num = models.CharField(max_length=10, verbose_name="房间号")
    total_bed = models.IntegerField(default=4, verbose_name="总床位数")
    remain_bed = models.IntegerField(default=4, verbose_name="剩余可用床位")

    class Meta:
        verbose_name = "宿舍信息"
        verbose_name_plural = verbose_name
        # 联合唯一约束：同一楼栋同一房间不重复
        unique_together = ("building", "room_num")

    def __str__(self):
        return f"{self.building}栋{self.room_num}室"