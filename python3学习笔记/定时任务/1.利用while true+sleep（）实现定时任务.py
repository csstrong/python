import datetime
import time

'''
位于 time 模块中的 sleep(secs) 函数，可以实现令当前执行的线程暂停 secs 秒后再继续执行。
所谓暂停，即令当前线程进入阻塞状态，当达到 sleep() 函数规定的时间后，再由阻塞状态转为就绪状态，等待 CPU 调度。
'''

def time_printer():
    now = datetime.datetime.now()
    ts = now.strftime('%Y-%m-%d %H:%M:%S')
    print('do func time:', ts)


def loop_monitor():
    while True:
        time_printer()
        time.sleep(5)  # 暂停5秒


if __name__ == "__main__":
    loop_monitor()
