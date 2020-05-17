#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 编写单元测试时，我们需要编写一个测试类，从unittest.TestCase继承。
import unittest
import re
from datetime import datetime, timedelta, timezone


def to_timestamp(dt_str, tz_str):
    utc_str = re.match(r'UTC([+-])(\d{1,2}):00', tz_str)
    # 正则得出utc
    utc_value = int(utc_str.group(2))
    # 取小时值
    utc = 1 if utc_str.group(1) == '+' else -1
    # 看正负
    utcv = utc_value * utc
    # 得出应该加或减
    tz_utc = timezone(timedelta(hours=utcv))
    # 创建时区
    dateUTC = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    # 将str转换成datetime
    dateUTC = dateUTC.replace(tzinfo=tz_utc)

    # 把utc改成input内容
    return dateUTC.timestamp()


class TestDict(unittest.TestCase):
    # datetime.now()返回当前日期和时间，其类型是datetime。
    def test_get_now(self):
        now = datetime.now()  # 获取当前datetime
        print(now)

        dt = datetime(2015, 4, 19, 12, 20)  # 用指定日期时间创建datetime
        print(dt)

    #     timestamp的值与时区毫无关系，因为timestamp一旦确定，其UTC时间就确定了，转换到任意时区的时间也是完全确定的，
    #     这就是为什么计算机存储的当前时间是以timestamp表示的，因为全球各地的计算机在任意时刻的timestamp都是完全相同的（假定时间已校准）。
    # 注意Python的timestamp是一个浮点数。如果有小数位，小数位表示毫秒数。
    def test_timestamp_and_datetime(self):
        # datetime到timestamp
        dt = datetime.now()
        timestamp = dt.timestamp()
        print(timestamp)

        # timestamp到datetime
        t = 1429417200.0
        print(datetime.fromtimestamp(t))  # 本地时间
        print(datetime.utcfromtimestamp(t))  # UTC时间

    # 注意转换后的datetime是没有时区信息的。
    def test_str_2_datetiem(self):
        cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
        print(cday)
        print(type(cday))
        print(isinstance(cday, datetime))

        # 如果已经有了datetime对象，要把它格式化为字符串显示给用户，就需要转换为str，转换方法是通过strftime()实现的，同样需要一个日期和时间的格式化字符串：
        now = datetime.now()
        print(now.strftime('%a, %b %d %H:%M'))

    # 对日期和时间进行加减实际上就是把datetime往后或往前计算，得到新的datetime。加减可以直接用+和-运算符，不过需要导入timedelta这个类：
    def test_operate_datetime(self):
        now = datetime.now()
        hours_ = now + timedelta(hours=10)
        print(hours_)

        print(now + timedelta(days=2, hours=12))

    # 本地时间是指系统设定时区的时间，例如北京时间是UTC+8:00时区的时间，而UTC时间指UTC+0:00时区的时间。
    def test_replace_zone(self):
        tz_utc_8 = timezone(timedelta(hours=8))  # 创建时区UTC+8:00
        now = datetime.now()
        dt = now.replace(tzinfo=tz_utc_8)  # 强制设置为UTC+8:00
        print(dt)

    # 时区转换的关键在于，拿到一个datetime时，要获知其正确的时区，然后强制设置时区，作为基准时间。
    #
    # 利用带时区的datetime，通过astimezone()方法，可以转换到任意时区。
    #
    # 注：不是必须从UTC+0:00时区转换到其他时区，任何带时区的datetime都可以正确转换，例如上述bj_dt到tokyo_dt的转换。
    def test_change_zone(self):
        # 拿到UTC时间，并强制设置时区为UTC+0:00:
        utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
        print(utc_dt)

        # astimezone()将转换时区为北京时间:
        bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
        print(bj_dt)

        # astimezone()将转换时区为东京时间:
        tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
        print(tokyo_dt)

        # astimezone()将bj_dt转换时区为东京时间:
        tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
        print(tokyo_dt2)

    # 如果你断言的 语句正确 则什么反应都没有
    # 但是如果你出错之后 就会报出    AssertionError 并且错误可以自己填写
    # 格式 ： assert+空格+要判断语句+双引号，“报错语句”
    # AssertionError: 1433121030.0
    def test_homework(self):
        # 测试:
        t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
        # assert t1 == 1433121031.0, t1
        try:
            assert t1 == 1433121031.0, ValueError("出错了")
        except AssertionError as e:
            print(e)

        t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
        assert t2 == 1433121030.0, t2

# if __name__ == "__main__":
#     # 这样就可以把mydict_test.py当做正常的python脚本运行：
#     # unittest.main()
#
#     # 另一种方法是在命令行通过参数 - m unittest直接运行单元测试：
#     # python -m unittest mydict_test
#     pass
