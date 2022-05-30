# 装饰器同样能传递参数

from schedule import every, repeat, run_pending
import time


@repeat(every().second, 'World')
@repeat(every().minute, 'python')
def greet(name):
    print('Hello', name)


while True:
    run_pending()
    time.sleep(1)
