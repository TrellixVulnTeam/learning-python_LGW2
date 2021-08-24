# -----------------------------------------------------
# learning-python
# Licensed under the GNU General Public License v3.0
# Written by Kaining (kennying99 {at} gmail.com)
# -----------------------------------------------------


"""
References:
    [1]: 一步一步教你认识Python闭包 - 没有回头的文章 - 知乎 https://zhuanlan.zhihu.com/p/26934085
    用最简单的语言解释Python的闭包是什么？ - Wayne的文章 - 知乎 https://zhuanlan.zhihu.com/p/59968665
"""


num = 1


def fun():
    global num
    num = 2


def print_msg():
    # print_msg 是外围函数
    msg = "zen of python"

    # nested function
    def printer():
        # printer是嵌套函数
        print(msg)
    printer()


# 用比较容易懂的人话说，就是当某个函数被当成对象返回时，夹带了外部变量，就形成了一个闭包。看例子。


def make_printer(msg):
    def printer():
        print(msg)  # 夹带私货（外部变量）
    return printer  # 返回的是函数，带私货的函数


# printer = make_printer('Foo!')
# printer()


def tag(tag_name):
    def add_tag(content):
        return "<{0}>{1}</{0}>".format(tag_name, content)
    return add_tag


content = 'Hello'

add_tag = tag('a')
print(add_tag(content))
# <a>Hello</a>

add_tag = tag('b')
print(add_tag(content))
# <b>Hello</b>


def make_printer(msg1, msg2, msg3):
    def printer():
        print(msg1, msg2, msg3)
    return printer


printer = make_printer('Foo', 'Bar', 'shit')

printer.__closure__
printer.__closure__[2].cell_contents




