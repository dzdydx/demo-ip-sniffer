# demo-ip-sniffer
为实验课编写的Django测试项目，用于简单地查询访问者公网IP。

由于没有配置服务器，因此打开了debug模式。

要运行Demo，请确保运行环境满足：
- Python >= 3.6
- Django >= 2.0

进入manage.py所在目录，然后执行
```
python manage.py runserver

# Or if you haven't set python 3 as default, run
python3 manage.py runserver
```

访问127.0.0.1:8000即可查看demo页面。