# 运行一次任务

import schedule
import time


def job_that_exectutes_once():
    print('hello')
    return schedule.CancelJob


schedule.every().minute.at(":05").do(job_that_exectutes_once)

while True:
    schedule.run_pending()
    time.sleep(1)
