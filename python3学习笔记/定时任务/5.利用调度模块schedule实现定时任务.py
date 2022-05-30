'''
schedule是一个第三方轻量级的任务调度模块，可以按照秒，分，小时，日期或者自定义事件执行时间。
schedule允许用户使用简单、人性化的语法以预定的时间间隔定期运行Python函数(或其它可调用函数)。
'''

import schedule
import time
import datetime


def time_printer():
    now = datetime.datetime.now()
    ts = now.strftime('%Y/%m/%d %H:%M:%S')
    print('do func time:', ts)


def job():
    time_printer()


schedule.every(10).seconds.do(job)
schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)
schedule.every(5).to(10).minutes.do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)
schedule.every().minutes.at(":17").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
