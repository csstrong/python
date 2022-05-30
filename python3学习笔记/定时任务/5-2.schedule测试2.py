# 装饰器:通过@request装饰静态方法

import time
from schedule import every, repeat, run_pending


@repeat(every().second)
def job():
    print('working...')


while True:
    run_pending()
    time.sleep(1)
