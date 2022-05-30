'''
threading 模块中的 Timer 是一个非阻塞函数，比 sleep 稍好一点，timer最基本理解就是定时器，
我们可以启动多个定时任务，这些定时器任务是异步执行，所以不存在等待顺序执行问题。
Timer(interval, function, args=[ ], kwargs={ })

interval: 指定的时间
function: 要执行的方法
args/kwargs: 方法的参数

Timer只能执行一次，这里需要循环调用，否则只能执行一次
'''

import datetime
from threading import Timer


def time_printer():
    now = datetime.datetime.now()
    ts = now.strftime('%Y/%m/%d %H:%M:%S')
    print('do func time:', ts)
    loop_monitor()


def loop_monitor():
    t = Timer(5, time_printer)
    t.start()


if __name__ == '__main__':
    loop_monitor()
