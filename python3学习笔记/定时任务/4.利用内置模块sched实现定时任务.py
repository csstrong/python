'''
sched模块实现了一个通用事件调度器，在调度器类使用一个延迟函数等待特定的时间，执行任务。
同时支持多线程应用程序，在每个任务执行后会立刻调用延时函数，以确保其他线程也能执行。

class sched.scheduler(timefunc, delayfunc)这个类定义了调度事件的通用接口，它需要外部传入两个参数，
timefunc是一个没有参数的返回时间类型数字的函数(常用使用的如time模块里面的time)，
delayfunc应该是一个需要一个参数来调用、与timefunc的输出兼容、并且作用为延迟多个时间单位的函数(常用的如time模块的sleep)。

scheduler对象主要方法:

enter(delay, priority, action, argument)，安排一个事件来延迟delay个时间单位。
-cancel(event)：从队列中删除事件。如果事件不是当前队列中的事件，则该方法将跑出一个ValueError。
-run()：运行所有预定的事件。这个函数将等待(使用传递给构造函数的delayfunc()函数)，然后执行事件，直到不再有预定的事件。

'''

import datetime
import time
import sched


def time_printer():
    now = datetime.datetime.now()
    ts = now.strftime('%Y/%m/%d %H:%M:%S')
    print('do func time:', ts)
    loop_monitor()


def loop_monitor():
    s = sched.scheduler(time.time, time.sleep)  # 生成调度器
    s.enter(5, 1, time_printer, ())
    s.run()


if __name__ == '__main__':
    loop_monitor()
