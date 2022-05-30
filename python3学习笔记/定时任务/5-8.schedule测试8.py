# 运行任务到某时间

import schedule
from datetime import datetime, timedelta, time


def job():
    print('working...')


schedule.every().second.until('23:59').do(job)  # 今天23:59停止
schedule.every().second.until('2022-10-10 18:30').do(job)  # 2022-10-10 18:30停止
schedule.every().second.until(timedelta(hours=8)).do(job)  # 8小时后停止
schedule.every().second.until(time(23, 59, 59)).do(job)  # 今天23:59:58停止
schedule.every().second.until(datetime(2022, 1, 1, 18, 30, 0)).do(job)  # 2022-01-01 18:30停止

while True:
    schedule.run_pending()
