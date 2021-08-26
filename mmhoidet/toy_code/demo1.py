# -----------------------------------------------------
# learning-python
# Licensed under the GNU General Public License v3.0
# Written by Kaining (kennying99 {at} gmail.com)
# -----------------------------------------------------



def func(num):
    if isinstance(num, (list, tuple, range)):
        return [func(n) for n in num]
    else:
        return num + 1


# @recursive(key='name', type='dict')
# def func(value, name):
#     return dict(name=value)


def func(value, name):
    if isinstance(name, (list, tuple, range)):
        out_dict = dict()
        for n in name:
            out_dict.update(func(value, n))
        return out_dict
    else:
        return dict(name=value)


print(func(['nba', 'cba'], [1, 2]))