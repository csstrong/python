# 传递参数

from schedule import every, repeat, run_pending


def greet(name):
    print('Hello', name)


every(2).seconds.do(greet, name='Alice')
every(4).seconds.do(greet, name='Bob')

while True:
    run_pending()
