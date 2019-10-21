# -*- coding:utf-8 -*-
import re
import math
def cosx(a,b):
    i = 0
    z = 0
    while i<len(a):
        z= z + a[i]*b[i]
        i = i + 1
    am = 0                                                 #计算a,b向量的模
    bm = 0
    for x1 in a:
        am=am + x1**2
    am = math.sqrt(am)
    for x2 in b:    
        bm=bm + x2**2
    bm = math.sqrt(bm)
    cosx = z/(am*bm)
    return cosx
    
class Passage():
    def __init__(self,path):
        self.path=path
    def cutarticle(self):                           #创建将文章分割的单词组成列表
        with open(self.path,'r') as f:
            c = re.split(" |!|\n|\t|\,|\.|\:",f.read())
            self.string = c
            return self.string
    def Words_number(self):                         #创建文章的总词数属性 
        self.number = len(self.string)
        return self.number
    def Words_sort(self):                            #计算前n位词出现的次数，降序排序
        with open(self.path,'r') as f:
            c = re.split(" |!|\n|\t|\,|\.|\:",f.read().lower())
            d = dict.fromkeys(c,0)                 #创建一个字典，key为出现过的单词，value初始值置为0
            for x in c:
                for key in d:
                    if x == key.lower():    #忽略大小写                
                        d[key] = d[key] + 1         #将单词和字典中的比对，计数
        d1 = d.items()                              #生成元组列表用于排序
        d2 = sorted(d1,key = lambda x:x[1],reverse = True)  #元组列表排序完毕
        i = 1                                       #监视哨
        wsort =[]                                   #将出现次数前n多的词及其出现次数组成一个列表，该列表按照词的出现次数降序排序
        for everyone in d2:
            if i>self.number//15:
                break
            elif everyone[0] == '':
                continue
            else:
                wsort.append(everyone)                       
                i = i + 1
        self.Wsort=wsort
    def Words_Frequency1(self):                            #创建词频(根据本文章)
        i = 1                                       #监视哨
        fre =[]                                    #创建词频列表
        for everyone in self.Wsort:
                fre.append((everyone[0],round(everyone[1]/self.number,8)))  #限制词频精度
                i = i + 1
        self.Fre=fre
    def Words_Frequency2(self,a):                        #创建词频(根据需要比对相似度的文章)
        with open(self.path,'r') as f:
            c = re.split(" |!|\n|\t|\,|\.|\:",f.read().lower())
            d = dict.fromkeys(c,0)                 
            for x in c:
                for key in d:
                    if x == key.lower():                        
                        d[key] = d[key] + 1         
        d1 = d.items()                              
        d2 = sorted(d1,key = lambda x:x[1],reverse = True)
        d3 = []                                    
        s = 0                                               #监视哨(是否找到该词)
        for x in a:
            d3.append(0)
        for x in a:
            for y in d2:
                if y[0] == x[0]:
                    d3[s]=((x[0],round(y[1]/self.number,8)))
            s = s + 1
        i = 0
        while i<len(d3):                                    #没有找的的单词置为("No",0)
            if d3[i] == 0:
                d3[i] = ("No",0)
            i = i + 1
        self.Fre=d3
    def get_Fre(self):                                     #获得词频
        return self.Fre
    def get_XFre(self):                                    #获得词频向量
        L = []
        for x in self.Fre:
            L.append(x[1])
        self.XFre = L
        return self.XFre
path1 = input("Please input the path of the first artical:")
passage1 =Passage(path1)
passage1.cutarticle()
passage1.Words_number()
passage1.Words_sort()
passage1.Words_Frequency1()
a = passage1.get_XFre()

path2 = input("Please input the path of the second artical:")
passage2 =Passage(path2)
passage2.cutarticle()
passage2.Words_number()
passage2.Words_sort()
c=passage1.get_Fre()
passage2.Words_Frequency2(c)
b = passage2.get_XFre()
print("两篇文章的相似度是",cosx(a,b))


