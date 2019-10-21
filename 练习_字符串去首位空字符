# -*- coding: utf-8 -*-
s=input("Please input a string:")
def trim(str):
    if s[0]=" ":
        newstr=s[1:]
    elif s[-1]=" ":
        newstr=s[:-1]
    return newstr
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')