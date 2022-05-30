# 马上运行所有任务（主要用于测试）

import schedule


def job():
    print('working...')


def job1():
    print('Hello...')


schedule.every().monday.at('12:40').do(job)
schedule.every().tuesday.at('16:40').do(job1)
schedule.run_all()
schedule.run_all(delay_seconds=3)  # 任务延迟3s
