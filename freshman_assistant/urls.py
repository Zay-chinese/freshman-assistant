from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# 导入所有接口视图
from api.views import UserView, DormView, CheckInView, PaymentView

# DRF框架自动生成API路由
router = DefaultRouter()
router.register(r'user', UserView)
router.register(r'dorm', DormView)
router.register(r'checkin', CheckInView)
router.register(r'payment', PaymentView)

urlpatterns = [
    # Django自带管理员后台
    path('admin/', admin.site.urls),
    # 所有前后端API接口统一前缀
    path('api/', include(router.urls)),
]