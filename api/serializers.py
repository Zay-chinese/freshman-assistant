from rest_framework import serializers
from users.models import User
from dormitory.models import Dormitory
from checkin.models import CheckInRecord
from payment.models import PaymentRecord

# 用户信息序列化器
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

# 宿舍信息序列化器
class DormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dormitory
        fields = "__all__"

# 报到记录序列化器
class CheckInSerializer(serializers.ModelSerializer):
    student = UserSerializer(read_only=True)
    dorm = DormSerializer(read_only=True)
    class Meta:
        model = CheckInRecord
        fields = "__all__"

# 缴费记录序列化器
class PaymentSerializer(serializers.ModelSerializer):
    student = UserSerializer(read_only=True)
    class Meta:
        model = PaymentRecord
        fields = "__all__"