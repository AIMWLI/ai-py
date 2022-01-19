import calendar
def clalendarDemo():
# 输入指定年月
    year = int(input("输入年份: "))
    month = int(input("输入月份: "))
# 显示日历
    print('\n'*2)
    print(calendar.month(year, month))
    return
clalendarDemo()