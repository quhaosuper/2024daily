import datetime
import random
import time
from dateutil.relativedelta import relativedelta


# 取当前系统日期零时
def datenow_zero():
    datenow = datetime.datetime.now()
    today_zero = datenow.strftime("%Y-%m-%d 00:00:00")
    return today_zero
    # print(today_zero)
    # print(type(today_zero))


def datenow_hms():
    datenow = datetime.datetime.now()
    today_hms = datenow.strftime("%Y%m%d%H%M%S") + str(random.randint(0, 999))
    return today_hms


def datenow_hmsf():
    datenow = datetime.datetime.now()
    today_hms = datenow.strftime("%Y%m%d%H%M%S%f")[:-3]
    return today_hms


def datenow_hms_ss():
    datenow = datetime.datetime.now()
    today_hms = datenow.strftime("%Y%m%d%H%M%S")
    return today_hms


def datenow_hms_s():
    datenow = datetime.datetime.now()
    today_hms = datenow.strftime("%m%d%H%M%S")
    return today_hms

# print(datenow_hmsf()[-10:])
# print(datenow_hms_ss())
# print(datenow_hms_s())


def datenow_timestamp():
    datenow = datetime.datetime.now()
    today_hms = datenow.strftime("%Y-%m-%d %H:%M:%S")
    time_stamp = time.mktime(time.strptime(today_hms, '%Y-%m-%d %H:%M:%S'))
    time_stamp = round(time_stamp)
    return time_stamp


def datenow_timestamp_plus(a):
    datenow = datetime.datetime.now() + relativedelta(days=a)
    today_hms = datenow.strftime("%Y-%m-%d %H:%M:%S")
    time_stamp = time.mktime(time.strptime(today_hms, '%Y-%m-%d %H:%M:%S'))
    time_stamp = round(time_stamp)
    return time_stamp


# 取次日零时
def datenextday():
    datenow = datetime.datetime.now() + datetime.timedelta(days=1)
    nextday = datenow.strftime("%Y-%m-%d 00:00:00")
    return nextday


def datenextday_single_hospital():
    datenow = datetime.datetime.now() + datetime.timedelta(days=4)
    nextday = datenow.strftime("%Y%m%d000000")
    return nextday


def dateplus_year(a):
    datenow_date = datetime.datetime.strptime(datenow_zero(), "%Y-%m-%d 00:00:00")
    datemin = (datenow_date + relativedelta(years=a)).strftime("%Y-%m-%d 00:00:00")
    return datemin
    # print(datemin)
    # print(type(datemin))


def dateplus_month(a):
    datenow_date = datetime.datetime.strptime(datenow_zero(), "%Y-%m-%d 00:00:00")
    datemin = (datenow_date + relativedelta(months=a)).strftime("%Y-%m-%d 00:00:00")
    return datemin
    # print(datemin)
    # print(type(datemin))


def dateplus_day(a):
    datenow_date = datetime.datetime.strptime(datenow_zero(), "%Y-%m-%d 00:00:00")
    datemin = (datenow_date + relativedelta(days=a)).strftime("%Y-%m-%d 00:00:00")
    return datemin
    # print(datemin)
    # print(type(datemin))


def dateplus_day_hms(a):
    datemin = (datetime.datetime.now() + relativedelta(days=a)).strftime("%Y-%m-%d %H:%M:%S")
    return datemin
    # print(datemin)
    # print(type(datemin))


# print(dateplus_day_hms(-30))


def dateplus_min(a):
    datemin = (datetime.datetime.now() + relativedelta(minutes=a)).strftime("%Y-%m-%d %H:%M:%S")
    return datemin


# print(dateplus_min(5))
# print(type(dateplus_min(5)))


# 取当前系统日期次年对应日期
def nextyear_desecond():
    datenow_date = datetime.datetime.strptime(datenow_zero(), "%Y-%m-%d %H:%M:%S")
    datenow_date = datenow_date + relativedelta(years=1)
    time_m = (datenow_date - datetime.timedelta(seconds=1)).strftime("%Y-%m-%d %H:%M:%S")
    return time_m
    # print(type(time_m))
    # print(time_m)


# 取当前日期次日次年对应的日期23:59:59
def nextmonth_desecond():
    datenow_date = datetime.datetime.strptime(datenow_zero(), "%Y-%m-%d %H:%M:%S")
    datenow_date = datenow_date + relativedelta(months=1)
    time_m = (datenow_date - datetime.timedelta(seconds=1)).strftime("%Y-%m-%d %H:%M:%S")
    return time_m
    # print(type(time_m))
    # print(time_m)


# 取当前日期次日次月对应的日期23:59:59
def nextyear_date():
    nextdate_date = datetime.datetime.strptime(datenextday(), "%Y-%m-%d %H:%M:%S")
    nextdate_date = nextdate_date + relativedelta(years=1)
    time_t = (nextdate_date - datetime.timedelta(seconds=1)).strftime("%Y-%m-%d 23:59:59")
    return time_t


def nextyear_single_date():
    nextdate_date = datetime.datetime.strptime(datenextday_single_hospital(), "%Y%m%d%H%M%S")
    nextdate_date = nextdate_date + relativedelta(years=1)
    time_t = (nextdate_date - datetime.timedelta(seconds=1)).strftime("%Y%m%d235959")
    return time_t


def longhu_orderno():
    data1 = time.time()
    data2 = int(data1)
    data3 = str(data2)
    data4 = 'LHAUTO' + data3
    return data4
    # print(data4)
    # print(type(data4))


def time_id():
    data1 = time.time()
    data2 = int(data1)
    data3 = str(data2)
    return data3


def time_now_year():
    now = datetime.date.today()
    year = now.year
    return year


def time_now_mon():
    now = datetime.date.today()
    month = now.month
    return month


# print(time_now_mon())
# datenow_zero()
# dateplus_year(1)
# dateplus_month(1)
# dateplus_day(10)
# nextyear_desecond()
# longhu_orderno()
# print(time_id())
