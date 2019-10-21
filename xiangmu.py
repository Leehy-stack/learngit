# -*- coding:utf-8 -*-
import re
class Words_counter():        #统计一篇英文短文中出现次数前十的单词
    def __init__(self,path):
        self.path=path
    def openfile(self):
        with open(self.path,'r') as f:
            s = f.read()
            print(s)
    def cutarticle(self):
        with open(self.path,'r') as f:
            c = re.split(" |!|\n|\t|\,|\.|\:",f.read())
            return c
    def add_words(self):
        with open(self.path,'r') as f:
            c = re.split(" |!|\n|\t|\,|\.|\:",f.read().lower())
            d = dict.fromkeys(c,0)                 #创建一个字典，key为出现过的单词，value初始值置为0
            for x in c:
                for key in d:
                    if x == key.lower():    #忽略大小写                
                        d[key] = d[key] + 1         #将单词和字典中的比对，计数
        d1 = d.items()                              #生成元组列表用于排序
        d2 = sorted(d1,key = lambda x:x[1],reverse = True)
        i = 1                                       #监视哨
        for everyone in d2:
            if i>10:
                return
            elif everyone[0] == '':
                continue
            else:
                print(everyone)
                i = i + 1
path1 = input("Please input the path of the first artical:")
counter1 = Words_counter(path1)
counter1.add_words()
path2 = input("Please input the path of the second artical:")
counter2 = Words_counter(path2)
counter2.add_words()
