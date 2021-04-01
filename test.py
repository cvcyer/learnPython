#!/usr/bin/env python
# -*- coding : utf-8 -*-
import os
# print("hello %s , you have %d money" % ('才艺',10000000))
# print("hello {0} , you tall is {1:.1f} m" .format('才艺',1.88))
# list = ["caiyi" , "caier" ,"caisan"]
# print(list)
# tuple = (1,)
# print(tuple)
# age=23
# if age >= 18:
#     print("older")
# elif age >=10:
#     print("study")
# else:
#     print("play play")
# names = ["caiy" , "cay" ,"cyyy"]
# for name in names:
#     print(name)
# for i in range(100):
#     print(i)
# sum = 0 
# n = 99
# while n > 0 :
#     sum = sum + n
#     n = n -2
# print(sum)
# d = {"caiyi":100 , "cyy":99}
# print(d["caiyi"])
# d["ccyy"] = 110
# print(d["ccyy"])
# bool = d.get("ccyy" , 0)
# print(bool)
# print(d)
# d.pop("cyy")
# print(d)

# s = set([1,2,3,4])
# print(s)
# s.add(8)
# s.add(8)
# print(s)
# s.remove(8)
# print(s)

# def my_abs(x):
#     if x >= 0:
#         return x
#     else:
#         raise TypeError("只允许输入正整数")
# i = -10
# print(my_abs(int(i)))

# def power (x , n=2):
#     s = 1
#     while n > 0 :
#         s=s*x
#         n=n-1
#     return s 
# print(power(5))

# def calc (*nums) :
#     sum = 0
#     for n in nums:
#         sum = sum + n*n
#     return sum
# print(calc(1,2,3))

# def person (name,age,**kw):
#     print("name:",name,"age:",age,"other:",kw)
# person("才艺",18,city="beijing",country="china")

# def person (name,age,*,country,sex):
#     print("name:",name,"age:",age,"country:",country,"sex:",sex)
# person("caiyi",18,country="china",sex="gg")

# def fact(n):
#     if n==1:
#         return 1
#     return n*fact(n-1)
# print(fact(1000))

# def fact(n):
#     return fact_iter(n, 1)

# def fact_iter(num, product):
#     if num == 1:
#         return product
#     return fact_iter(num - 1, num * product)
# print(fact(1000))

# L = ["caiyi" , "ccyy" ,"cyy"]
# print(L)
# # print(L[0:3])
# print(L[-2:-1])

# L = list(range(101))
# print(L)
# print(L[0:11])
# print(L[0:10:5])

# s="today is fine"
# print(s[::2])

# print("today is fine"[::2])


# dic = {"caiyi":100 , "ccyy":99 , "cy":98}
# for i in dic.values():
#     print(i)
# from collections import Iterable
# a = isinstance(dic,Iterable)
# print(a)
# for i , v in enumerate(dic):
    # print(i,v)

# list = ["caiyi","ccyy"]
# for i , v in enumerate(list):
#     print(i,v)

# list = [x*x for x in range(1,11)]
# print(list)

# list = [x*x for x  in range(1,11) if x%2 == 0]
# print(list)

# list = [m+n for m in "abc" for n in "def"]
# print(list)

# list = [d for d in os.listdir()]
# print(list)

# list = list(range(1,111))
# print(list)

# g = (x*x for x in range(1,111111))
# for i in g:
#     print(i)

#斐波拉契数列  1 1 2 3 5 8 13
# def fib(max):
#     n , a , b = 0 , 0 ,1
#     while n < max:
#         # print(b)
#         yield b
#         a , b = b , a+b
#         n=n+1
#     return 'completed'
# for i in fib(10):
#     print(i)
# from collections.abc import Iterable
# print(isinstance(fib,Iterable))
# from collections.abc import Iterator
# print(isinstance(fib,Iterator))

def all(x):
    n=0
    while n < x:
        yield n
        n = n +1
    return "completed"
for i in all(1000000000000000000):
    print(i)