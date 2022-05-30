# 并行运行：使用python内置队列实现

import schedule
import threading
import time


def job1():
    print('i am running on thread %s' % threading.current_thread())


def job2():
    print('i am running on thread %s' % threading.current_thread())


def job3():
    print('i am running on thread %s' % threading.current_thread())


def run_thread(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()


schedule.every(10).seconds.do(run_thread, job1)
schedule.every(10).seconds.do(run_thread, job2)
schedule.every(10).seconds.do(run_thread, job3)

while True:
    schedule.run_pending()
    time.sleep(1)
