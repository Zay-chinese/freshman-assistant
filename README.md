# freshman-assistant
大学新生报到智能助手 | 智慧校园迎新微信小程序项目
大学新生报到智能助手
项目简介
本项目是一个面向高校新生报到场景的一站式智能管理系统，旨在解决传统新生报到流程繁琐、信息分散、管理效率低下的问题。系统采用前后端分离架构，后端基于 Django REST Framework 开发，提供完整的 RESTful API 接口，支持对接 Web 前端或微信小程序。系统包含新生信息管理、报到流程管理、宿舍分配管理、缴费状态管理四大核心模块，并提供功能完善的管理员后台，实现对新生报到全流程的数字化、智能化管理。
功能特性
1. 用户管理模块
支持两种用户角色：系统管理员、在校新生
基于 Django 内置认证系统扩展的自定义用户模型
支持学号、手机号、专业、性别等扩展字段
完整的用户增删改查功能
管理员后台可视化用户管理
2. 新生报到模块
新生报到状态管理（待报到 / 已完成 / 已驳回）
报到时间自动记录
管理员备注功能
报到记录与用户一对一关联
支持按报到状态筛选查询
3. 宿舍管理模块
宿舍信息管理（楼栋号、房间号、床位数）
剩余床位自动统计
宿舍与新生报到记录关联
支持手动分配宿舍
联合唯一约束防止重复宿舍信息
4. 缴费管理模块
新生缴费记录管理
缴费状态跟踪（未缴费 / 已缴费）
缴费金额和时间记录
支持按缴费状态筛选查询
缴费记录与用户多对一关联
5. 系统管理功能
Django 原生强大的管理员后台
支持数据批量导入导出
灵活的权限控制
完整的操作日志
支持自定义后台展示字段和筛选条件
6. API 接口功能
基于 Django REST Framework 的 RESTful API
自动生成 API 文档和可视化接口页面
支持跨域请求，方便前端对接
统一的 JSON 数据返回格式
完整的 CRUD 接口支持
技术栈
后端技术
编程语言：Python 3.9+
Web 框架：Django 4.2.30
API 框架：Django REST Framework 3.16.1
跨域处理：django-cors-headers 4.9.0
ORM 框架：Django ORM
认证系统：Django 内置认证系统
数据库
开发环境：SQLite3（Django 内置，无需额外配置）
生产环境：支持 MySQL 8.0+、PostgreSQL 14+
开发与部署工具
开发工具：Visual Studio Code
虚拟环境：Python venv
版本控制：Git
生产部署：Nginx + Gunicorn + Supervisor
操作系统：支持 Windows、Linux、
项目结构
plaintext
freshman-assistant/
├── api/                     # API接口模块
│   ├── __init__.py
│   ├── views.py             # 接口视图
│   └── serializers.py       # 数据序列化器
├── checkin/                 # 新生报到模块
│   ├── __init__.py
│   ├── models.py            # 报到数据模型
│   └── admin.py             # 后台注册
├── dormitory/               # 宿舍管理模块
│   ├── __init__.py
│   ├── models.py            # 宿舍数据模型
│   └── admin.py             # 后台注册
├── payment/                 # 缴费管理模块
│   ├── __init__.py
│   ├── models.py            # 缴费数据模型
│   └── admin.py             # 后台注册
├── users/                   # 用户管理模块
│   ├── __init__.py
│   ├── models.py            # 自定义用户模型
│   └── admin.py             # 后台注册
├── freshman_assistant/      # 项目主配置目录
│   ├── __init__.py
│   ├── settings.py          # 全局配置文件
│   ├── urls.py              # 总路由配置
│   ├── asgi.py
│   └── wsgi.py
├── venv/                    # Python虚拟环境
├── db.sqlite3               # SQLite数据库文件
├── manage.py                # Django项目管理脚本
├── start.bat                # Windows一键启动脚本
├── requirements.txt         # 项目依赖清单
├── .gitignore               # Git忽略文件
├── LICENSE                  # 许可证文件
└── README.md                # 项目说明文档
快速开始
环境准备
Python 3.9 或更高版本
pip 包管理工具
Git（可选）
本地开发部署
1. 获取项目代码
bash
运行
# 克隆项目（如果使用Git）
git clone https://github.com/your-username/freshman-assistant.git
cd freshman-assistant

# 或者直接解压项目压缩包到本地目录
2. 创建并激活虚拟环境
bash
运行
# Windows系统
python -m venv venv
venv\Scripts\activate.bat

# Linux/macOS系统
python3 -m venv venv
source venv/bin/activate
3. 安装项目依赖
bash
运行
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
4. 数据库迁移
bash
运行
# 生成数据库迁移文件
python manage.py makemigrations

# 应用迁移，创建数据表
python manage.py migrate
5. 创建超级管理员
bash
运行
python manage.py createsuperuser
按照提示输入用户名、邮箱（可留空）和密码。
6. 启动开发服务器
bash
运行
# 方式一：直接启动
python manage.py runserver

# 方式二：使用一键启动脚本（Windows）
双击 start.bat 文件
7. 访问系统
管理员后台：http://127.0.0.1:8000/admin/
API 接口文档：http://127.0.0.1:8000/api/
生产环境部署
服务器环境准备
操作系统：Ubuntu 20.04 LTS 或 CentOS 8+
Python 3.9+
Nginx
MySQL 8.0+（推荐生产环境使用）
部署步骤
1. 服务器环境配置
bash
运行
# 更新系统
sudo apt update && sudo apt upgrade -y

# 安装Python和依赖
sudo apt install python3 python3-pip python3-venv nginx mysql-server -y
2. 项目上传与配置
bash
运行
# 创建项目目录
sudo mkdir -p /var/www/freshman-assistant
sudo chown -R $USER:$USER /var/www/freshman-assistant

# 上传项目代码到服务器
# 可以使用scp、git或FTP工具

# 创建并激活虚拟环境
cd /var/www/freshman-assistant
python3 -m venv venv
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt
pip install gunicorn
3. 生产环境配置修改
编辑 freshman_assistant/settings.py 文件：
python
运行
# 关闭调试模式
DEBUG = False

# 允许的主机头
ALLOWED_HOSTS = ['your-domain.com', '服务器IP地址']

# 修改数据库配置（使用MySQL）
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'freshman_db',
        'USER': 'db_user',
        'PASSWORD': 'db_password',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8mb4'
        }
    }
}

# 静态文件配置
STATIC_ROOT = '/var/www/freshman-assistant/static/'
4. 收集静态文件
bash
运行
python manage.py collectstatic
5. 配置 Gunicorn
创建 /etc/systemd/system/freshman.service 文件：
ini
[Unit]
Description=Freshman Assistant Gunicorn daemon
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/var/www/freshman-assistant
ExecStart=/var/www/freshman-assistant/venv/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/var/www/freshman-assistant/freshman.sock \
          freshman_assistant.wsgi:application

[Install]
WantedBy=multi-user.target
启动并设置开机自启：
bash
运行
sudo systemctl start freshman
sudo systemctl enable freshman
6. 配置 Nginx
创建 /etc/nginx/sites-available/freshman 文件：
nginx
server {
    listen 80;
    server_name your-domain.com 服务器IP地址;

    location /static/ {
        alias /var/www/freshman-assistant/static/;
    }

    location / {
        proxy_pass http://unix:/var/www/freshman-assistant/freshman.sock;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
启用配置并重启 Nginx：
bash
运行
sudo ln -s /etc/nginx/sites-available/freshman /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
API 文档
系统提供完整的 RESTful API 接口，所有接口均返回 JSON 格式数据。
基础信息
基础 URL：http://your-domain.com/api/
数据格式：JSON
编码格式：UTF-8
核心接口列表
表格
接口路径	请求方法	说明
/api/user/	GET	获取所有用户列表
/api/user/	POST	创建新用户
/api/user/{id}/	GET	获取指定用户详情
/api/user/{id}/	PUT	更新指定用户信息
/api/user/{id}/	DELETE	删除指定用户
/api/dorm/	GET	获取所有宿舍列表
/api/dorm/	POST	创建新宿舍
/api/checkin/	GET	获取所有报到记录
/api/checkin/	POST	创建新报到记录
/api/payment/	GET	获取所有缴费记录
/api/payment/	POST	创建新缴费记录
完整的 API 文档可以在启动项目后访问：http://127.0.0.1:8000/api/
常见问题
Q1: 启动项目时提示 ModuleNotFoundError: No module named 'rest_framework'
A: 没有安装项目依赖，执行 pip install -r requirements.txt 即可解决。
Q2: 访问根地址 http://127.0.0.1:8000/ 显示 404 错误
A: 项目默认没有配置根路径首页，直接访问管理员后台 http://127.0.0.1:8000/admin/ 或 API 接口 http://127.0.0.1:8000/api/ 即可。
Q3: 局域网内其他设备无法访问项目
A: 启动项目时使用 python manage.py runserver 0.0.0.0:8000 命令，并在 Windows 防火墙中允许 Python 通过防火墙。
Q4: 忘记管理员密码怎么办
A: 在虚拟环境中执行 python manage.py changepassword admin 命令，按照提示重置密码。
开发规范
代码规范
遵循 PEP 8 Python 代码规范
使用 4 个空格缩进
变量和函数使用小写字母加下划线命名
类名使用大驼峰命名法
关键代码添加必要的注释
提交规范
提交信息格式：类型: 简短描述
类型包括：feat (新功能)、fix (修复 bug)、docs (文档)、style (格式)、refactor (重构)、test (测试)、chore (构建)
更新日志
v1.0.0 (2026-04-27)
完成项目核心功能开发
实现用户、报到、宿舍、缴费四大模块
提供完整的管理员后台
生成全套 RESTful API 接口
完成本地开发环境部署文档
许可证
本项目采用 MIT 许可证 开源，可自由使用、修改和分发。







把项目简介部分的字数精简到100字左右
生成一个包含项目背景、功能特性、技术架构的Markdown文件
推荐一些优秀的Markdown文档示例
