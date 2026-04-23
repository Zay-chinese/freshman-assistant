大学新生报到智能助手 - 技术方案 V2.0   张骜元

一、执行摘要
#本方案基于 MVP 最小可行产品 设计原则，面向校内 500 人以内新生用户规模，采用 Django + PostgreSQL 技术栈，构建轻量、易部署、易维护、可扩展的新生报到全流程管理系统。
#方案覆盖：总体架构、技术选型、项目主体框架、核心模块、MVP 功能、数据库设计、接口设计、开发计划、部署方案。
确保初代版本 代码可完整运行、基础业务闭环、本地环境全流程跑通，并预留微服务、云部署、AI 扩展能力。
二、系统总体架构
2.1 四层架构设计（前后端分离）
表现层：微信小程序（新生）+ Web 管理后台（校方）
接口层：统一 API 入口、请求鉴权、数据格式封装
业务逻辑层：Django 后端，负责核心流程、权限、数据校验、业务调度
数据持久层：PostgreSQL 数据库，负责数据存储与事务保障
2.2 架构流程图
flowchart TD
    A[新生报到智能助手] --> B[新生端 微信小程序]
    A --> C[管理端 Web 后台]
    A --> D[API 接口层]
    D --> E[Django 业务逻辑层]
    E --> F[PostgreSQL 数据库]
新生报到智能助手

新生端 微信小程序

管理端 Web 后台

API 接口层

Django 业务逻辑层

PostgreSQL 数据库

三、核心技术栈
3.1 后端技术
框架：Django 4.2.30（稳定 LTS 版本）
接口：Django REST Framework
数据库：PostgreSQL
环境：Python 3.10+ + 虚拟环境 venv
安全：django-cors-headers（跨域）
版本管理：Git + GitHub

3.2 技术优势
开箱即用，自带 ORM、Admin 后台、权限系统
开发速度快，适合 MVP 快速落地
数据安全、事务稳定，适合学籍 / 报到类业务
架构规范，便于团队协作与后期扩展

四、项目主体框架（你当前已实现的完整结构）
plaintext
freshman-assistant/           # 项目根目录
├── freshman_assistant/       # Django 主项目（全局配置中心）
│   ├── __init__.py
│   ├── settings.py           # 全局配置
│   ├── urls.py               # 总路由
│   ├── asgi.py
│   └── wsgi.py
├── users/                    # 用户模块（新生/管理员）
├── checkin/                  # 报到业务模块
├── dormitory/                # 宿舍管理模块
├── payment/                  # 缴费管理模块
├── api/                      # 统一 API 接口模块
├── manage.py                 # 项目启动入口
└── requirements.txt          # 依赖清单

五、核心模块说明（MVP 必选）
5.1 users（用户中心）
用户登录、身份验证
新生信息管理
角色区分：新生 / 管理员
基础信息：学号、姓名、电话、身份证、专业

5.2 checkin（报到核心）
预报到提交
报到状态：待审核 / 已完成
报到时间记录
与用户、宿舍关联

5.3 dormitory（宿舍管理）
楼栋、房间号、床位数、剩余床位
宿舍分配记录
后台可维护

5.4 payment（缴费管理）
缴费状态标记
简单缴费记录
MVP 仅做状态管理

5.5 api（接口统一出口）
提供小程序 / 前端所有接口
数据序列化、权限控制
统一返回格式

六、MVP 最小可用功能（第一代程序可完整跑通）

6.1 新生端（小程序可调用）
新生登录 / 信息查看
填写个人信息并提交预报到
查看报到状态
查看分配的宿舍
查看缴费状态

6.2 管理端（Django Admin 自动生成）
管理员登录后台
查看 / 编辑 / 删除新生信息
审核报到申请
管理宿舍信息
查看报到统计

6.3 后端基础能力
完整数据库表结构
全套 API 接口
权限控制
数据校验
本地可运行、可测试、可联调

七、数据库 ORM 模型设计（核心 4 张表）

7.1 User（用户表）
python
运行
class User(AbstractUser):
    role = models.CharField(choices=[('student','新生'),('admin','管理员')])
    student_id = models.CharField('学号')
    phone = models.CharField('电话')
    id_card = models.CharField('身份证')

7.2 Dormitory（宿舍表）
python
运行
class Dormitory(models.Model):
    building = models.CharField('楼栋')
    room_number = models.CharField('房间号')
    bed_count = models.IntegerField('总床位')
    available_beds = models.IntegerField('剩余床位')

7.3 CheckInRecord（报到记录表）
python
运行
class CheckInRecord(models.Model):
    student = models.OneToOneField(User)
    dormitory = models.ForeignKey(Dormitory)
    checkin_time = models.DateTimeField('报到时间', null=True)
    status = models.CharField('状态', choices=[('pending','待报到'),('completed','已报到')])
    is_paid = models.BooleanField('是否缴费')

7.4 PaymentRecord（缴费记录表）
python
运行
class PaymentRecord(models.Model):
    student = models.ForeignKey(User)
    amount = models.DecimalField('金额', max_digits=10, decimal_places=2)
    pay_time = models.DateTimeField('缴费时间', null=True)
    status = models.BooleanField('缴费状态')

八、API 接口清单（MVP 必备）
plaintext
/api/users/           # 用户列表/详情
/api/checkin/         # 报到提交/查询/状态修改
/api/dormitories/      # 宿舍列表
/api/payments/        # 缴费记录
/admin/               # 管理后台

九、完整开发计划（你可直接按此执行）
阶段 1：环境搭建（✅ 已完成）
虚拟环境、Django 安装
项目创建、5 大 App 生成
推送到 GitHub
本地服务可运行
阶段 2：全局配置（进行中）
注册 App
中文 / 时区配置
跨域、DRF 配置
PostgreSQL 连接
阶段 3：模型 + 数据库（核心）
编写 4 张表模型
执行数据库迁移
注册到 Admin 后台
阶段 4：API 接口开发
序列化器编写
视图编写
路由配置
接口调试
阶段 5：MVP 联调测试
全流程跑通
提交代码
完成第一代可运行版本

十、本地运行方案（重启电脑通用）
bash
运行
# 1. 进入项目文件夹
D:\freshman-assistant

# 2. 打开 CMD
地址栏输入 cmd 回车

# 3. 激活虚拟环境
venv\Scripts\activate.bat

# 4. 启动服务
python manage.py runserver
访问：
前端：http://127.0.0.1:8000
管理后台：http://127.0.0.1:8000/admin

十一、版本规划
V2.0（当前目标）
框架完整
模型完整
API 完整
本地可跑通
MVP 功能闭环
V2.1（扩展）
完善前端界面
增加消息通知
优化权限
V3.0（完整版）
AI 问答
云服务器部署
Docker 容器化
十二、总结
本方案 100% 贴合你已搭建的 Django 项目结构，严格按照 MVP 原则设计，确保第一代程序能够：
完整跑通
功能可用
结构规范
可直接用于课程设计 / 毕业设计
可继续扩展升级