# -*- coding: utf-8 -*-
import time, functools
def metric(fn):              #计算函数执行时间装饰器
    @functools.wraps(fn)
    def wrapper(*args,**kw):
        start = time.time()
        result = fn(*args,**kw)
        end = time.time()
        print("函数执行时长：",end - start)
        return result
    return wrapper