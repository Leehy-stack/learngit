# -*- coding:utf-8 -*-
import re
import math
class Passage():
    def __init__(self,path):
        self.path=path
    def cutarticle(self):                           #将分割的单词组成列表
        with open(self.path,'r') as f:
            c = re.split(" |!|\n|\t|\,|\.|\:",f.read())
            self.string = c
            return self.string
    def Words_number(self):
        self.number = len(self.string)
        return self.number
    def (self):
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
passage1 = Passage()