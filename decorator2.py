# -*- coding: utf-8 -*-
import functools
def log_for_two (fn):
    i=int(input("Please input the ggg:"))
    def log(text):
        def decorator(fn):
            @functools.wraps(fn)
            def wrapper(*args, **kw):
                if (i==1):
                    print('%s %s():' % (text, fn.__name__))
                else :
                    print('call %s():' % func.__name__)
                return fn(*args, **kw)
            return wrapper
        return decorator