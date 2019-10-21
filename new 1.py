# -*- coding:utf-8 -*-
class Words_counter():        #统计一篇英文短文中出现次数前十的单词
    def __init__(self,path):
        self.path=path
    def openfile1(self):
        with open(path,'r') as f:
            s = f.read()
            print(s)
path1 = input("Please input the path of first artical:")
counter1 = Word_counter(path1) 