from rest_framework import viewsets
from users.models import User
from dormitory.models import Dormitory
from checkin.models import CheckInRecord
from payment.models import PaymentRecord
from .serializers import UserSerializer, DormSerializer, CheckInSerializer, PaymentSerializer

# 用户信息接口
class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# 宿舍信息接口
class DormView(viewsets.ModelViewSet):
    queryset = Dormitory.objects.all()
    serializer_class = DormSerializer

# 新生报到接口
class CheckInView(viewsets.ModelViewSet):
    queryset = CheckInRecord.objects.all()
    serializer_class = CheckInSerializer

# 缴费记录接口
class PaymentView(viewsets.ModelViewSet):
    queryset = PaymentRecord.objects.all()
    serializer_class = PaymentSerializer