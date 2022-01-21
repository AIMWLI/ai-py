# mysql-client常见问题
## debug
```PYTHONUNBUFFERED=1;DJANGO_SETTINGS_MODULE=djangoProject.settings```

## 找不到_mysql
I was facing the same problem on my MacOS (Big Sur) and I fixed it by doing this 
```cp -r /usr/local/mysql/lib/* /usr/local/lib/```

## 初始化表
python manage.py makemigrations [app_name]
<br>
python manage.py migrate
