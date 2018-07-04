#!/usr/bin/python

from random import randint

f1=open('D:/1.fastq','r')
f2=open('D:/10%_fastq_split1.txt','w')
list1=f1.readlines()
list2=[line for line in list1 if ('@' in line)] ###生成仅包含“@”行的列表
list3=[]
x=len(list1)    ###fastq总行数
k=int(0.25*x)   ###“k”为fastq所含的序列条目的数量
while k>=int(0.25*0.9*x):
    n=randint(0,k-1)
    list2.pop(n)    ###每抽取一个n值，向新列表中写入相应的行，并从抽样池中删除
    list3.append(list1[4*n])
    list3.append(list1[4*n+1])
    list3.append(list1[4*n+2])
    list3.append(list1[4*n+3])  ###fastq文件中找到对应的第4n行写入
    list1.pop(4*n)
    list1.pop(4*n)
    list1.pop(4*n)
    list1.pop(4*n)  ###依次删除以写入新列表的行
    k+=-1

f2.writelines(list3)
f2.close()
print ('Check file "D:/10%_fastq_split1.txt"')








######  Solution 2很慢: random.sample  #######
import random

fx=open('D:/1.fastq','r')
fy=open('D:/10%_fastq_split2.txt','w')
listx=fx.readlines()
listy=[line for line in listx if ('@' in line)]
a=int(0.1*len(listy))
listz=random.sample(listy,a)    ###sample方法为随机且不重复抽样
list_fy=[]

for line in listz:
    m=listx.index(line)     ### "m"为该条序列在fastq文件中的下标数字
    list_fy.append(listx[m])
    list_fy.append(listx[m+1])
    list_fy.append(listx[m+2])
    list_fy.append(listx[m+3])

fy.writelines(list_fy)
fy.close()
print ('Check file "D:/10%_fastq_split2.txt"')
