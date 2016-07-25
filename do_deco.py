# -*- coding: utf-8 -*-
from functools import wraps

import time


def time_this(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result
    return wrapper


@time_this
def count_down(n):
    """统计时间
    :param n
    :return: no
    """
    while n > 0:
        n -= 1


if __name__ == '__main__':
    count_down(3000000)
    print(count_down.__name__)
    print(count_down.__doc__)
    print(count_down)