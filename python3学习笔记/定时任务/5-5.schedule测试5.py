# 取消任务

import schedule

i = 0


def some_task():
    global i
    i += 1
    print(i)
    if i == 10:
        schedule.cancel_job(job)
        print('cancel job')
        exit(0)


job = schedule.every().second.do(some_task)
while True:
    schedule.run_pending()
