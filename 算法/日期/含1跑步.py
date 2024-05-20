"""
作者：legionb
日期：2024年05月20日
"""
import datetime as dt

months=[1,10,11,12]
big=[1,3,5,7,8,10,12]
big_days=[1,10,11,12,13,14,15,16,17,18,19,21,31]
small_days=[1,10,11,12,13,14,15,16,17,18,19,21]

cur=dt.datetime(2023,1,1)
end=dt.datetime(2023,12,31)
delta=dt.timedelta(days=1)
res=0

while cur<=end:
    month=cur.month
    day = cur.day
    if month in months:
        res +=5
    elif month in big and day in big_days or month not in big and day in small_days:
        res+=5
    elif cur.weekday()==0:
        res+=5
    else:
        res+=1
    cur+=delta

print(res)
print(end)
