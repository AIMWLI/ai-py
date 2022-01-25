import arrow

# 获取世界标准时间
utcnow = arrow.utcnow()
print(utcnow)  # 2021-09-19T02:56:00.435537+00:00

# 获取指定时区的时间
utc = arrow.now('Asia/Shanghai')
print(utc)  # 2021-09-19T10:58:44.183601+08:00

# 将时间戳转化为arrow对象
print(arrow.get(1519534533))  # 2018-02-25T04:55:33+00:00

# 格式化转换
print(arrow.get('2018-02-24 12:30:45',
                'YYYY-MM-DD HH:mm:ss'))  # 2018-02-24T12:30:45+00:00

# 遵循ISO-8601的字符串不需要格式字符串参数即可转换
print(arrow.get('2018-02-24T13:00:00.000-07:00'))  # 2018-02-24T13:00:00-07:00

# 通过时间元组进行创建,arrow.get()或arrow.Arrow()
print(arrow.get(2018, 2, 24))  # 2018-02-24T00:00:00+00:00
print(arrow.Arrow(2018, 2, 24))  # 2018-02-24T00:00:00+00:00

# 获取datetime时间
a = arrow.now()
print(a.datetime)  # 2021-09-19 11:37:57.579250+08:00

# 获取年
a = arrow.now()
print(a.year)
print(a.month)
print(a.day)
print(a.minute)
print(a.hour)
print(a.second)

# 时间戳
timestamp = arrow.now().timestamp()
print(timestamp)

# 时间推移
# shift方法获取某个时间之前或之后的时间,关键字参数为years,months,weeks,days,hours，seconds，microseconds
# 三周后
now = arrow.now()
print(now.shift(weeks=+3))  # 2022-02-15T14:11:26.163611+08:00
# 一天前
print(a.shift(days=-1))  # 2022-01-24T14:11:26.163520+08:00
# 距离最近的星期日
print(a.shift(weekday=6))  # 2021-09-19T17:31:21.434495+08:00

# 时间替换
replace = arrow.now().replace(hour=9)
