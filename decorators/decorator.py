# -----------------------------------------------------
# learning-python
# Licensed under the GNU General Public License v3.0
# Written by Kaining (kennying99 {at} gmail.com)
# -----------------------------------------------------

"""
References:
    [1]: https://www.zhihu.com/search?type=content&q=python%20%E8%A3%85%E9%A5%B0%E5%99%A8
    [2]: Python 装饰器为什么难理解？ - 刘志军的文章 - 知乎 https://zhuanlan.zhihu.com/p/27449649
    [3]: https://www.liaoxuefeng.com/wiki/1016959663602400/1017451662295584
"""


from time import time, sleep


def fun_one():
    start = time()
    sleep(1)
    end = time()
    cost_time = end - start
    print("function one runs time {}".format(cost_time))


def fun_two():
    start = time()
    sleep(1)
    end = time()
    cost_time = end - start
    print("function two runs time {}".format(cost_time))


def fun_three():
    start = time()
    sleep(1)
    end = time()
    cost_time = end - start
    print("function three runs time {}".format(cost_time))


def run_time(func):
    def wrapper():
        start = time()
        func()                  # 函数在这里运行
        end = time()
        cost_time = end - start
        print("function three runs time {}".format(cost_time))
    return wrapper


@run_time
def fun_one():
    sleep(1)


@run_time
def fun_two():
    sleep(1)


@run_time
def fun_three():
    sleep(1)


def logger(msg=None):
    def run_time(func):
        def wrapper(*args, **kwargs):
            start = time()
            func()                  # 函数在这里运行
            end = time()
            cost_time = end - start
            print("[{}] function three runs time {}".format(msg, cost_time))
        return wrapper
    return run_time


@logger(msg="One")
def fun_one():
    sleep(1)


@logger(msg="Two")
def fun_two():
    sleep(1)


@logger(msg="Three")
def fun_three():
    sleep(1)


def foo(num):
    return num + 1


def bar(fun):
    return fun(3)


def outer():
    x = 1

    def inner():
        print(x)
    inner()


def outer(func):
    def inner():
        print("记录日志开始")
        func()  # 业务函数
        print("记录日志结束")
    return inner


def foo():
    print("foo")


def logger(msg=None):
    def run_time(func):
        def wrapper(*args, **kwargs):
            start = time()
            func()  # 函数在这里运行
            end = time()
            cost_time = end - start
            print("[{}] func three run time {}".format(msg, cost_time))

        return wrapper

    return run_time


@logger(msg="One")
def fun_one():
    sleep(1)


@logger(msg="Two")
def fun_two():
    sleep(1)


@logger(msg="Three")
def fun_three():
    sleep(1)


def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log('execute')
def now():
    print('2015-3-25')


if __name__ == '__main__':
    # value = bar(foo)
    # print(value)

    # outer()  # 1

    # foo = outer(foo)
    # foo()

    # fun_one()
    # fun_two()
    # fun_three()

    now()


