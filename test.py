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

# 斐波拉契数列  1 1 2 3 5 8 13
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

# def all(x):
#     n=0
#     while n < x:
#         yield n
#         n = n +1
#     return "completed"
# for i in all(1000000000000000000):
#     print(i)


# def f(x):
#     return x*x
# r = map (f,[1,2,3,4])
# for i in r:
#     print(i)

# from functools import reduce
# def add(x,y):
#     return x+y
# r = reduce(add,[1,2,3,4,5])
# print(r)

# from functools import reduce
# def fn(x,y):
#     return x*10+y
# s = reduce(fn,[1,2,3,4,5])
# print(s)

# def is_odd(n):
#     return n % 2 == 0
# print(list(filter(is_odd,[1,2,3,4,5])))


# def odd_iter():
#     n=1
#     while True:
#         n = n+2
#         yield n
# # odd_iter是一个生成器
# def not_divisible(n):
#     return lambda x: x%n > 0
# def primes():
#     yield 2
#     it = odd_iter()
#     while True:
#         n = next(it)
#         yield n 
#         it = filter(not_divisible,it)
# for i in primes():
#     if i < 100:
#         print(i)


# def calc_sum(*args):
#     ex = 0
#     for n in args:
#         ex= ex+ n
#     return ex
# print(calc_sum(1,2,3,4,5))

# def lazy_sum(*args):
#     def sum():
#         ex = 0
#         for i in args:
#             ex = ex + i
#         return ex
#     return sum
# f = lazy_sum(1,2,3,4,5)
# f2 = lazy_sum(1,2,3,4,5)
# print(f == f2)
# print(f())
# print(f2())
# print(f)
# print(f())

# def count():
#     def f(j):
#         def g():
#             return j*j
#         return g
#     fs = []
#     for i in range(1,4):
#         fs.append(f(i))
#     return fs
# for i in count():
#     print (i())

# l = list(map(lambda x : x*x , [1,2,3,4,5]))
# for i in l:
#     print(i)

# def add(*x):
#     sum = 0 
#     for i in x:
#         sum = sum + i
#     return sum
# # print(add.__name__)
# print(add(1,2,3,4,5))
# print(add.__name__)

# def log(func):
#     def wrappar(*args , **kw):
#         print("call %s():" % func.__name__)
#         return func(*args,**kw)
#     return wrappar
# @log
# def now():
#     print("打印一行")
# print(now())

# def log(text):
#     def decorator(func):
#         def wrapper(*args,**kw):
#             print("%s %s:" % (text,func.__name__))
#             return func(*args,**kw)
#         return wrapper
#     return decorator
# @log("execute")
# def now():
#     print("2021/04/02")
# now()

# import functools

# def log(text):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper (*args , **kw):
#             print("%s %s():" % (text,func.__name__))
#             return func(*args , **kw)
#         return wrapper
#     return decorator

# @log("call : " )
# def now():
#     print("2020111")
# print(now())

# import functools

# int2 = functools.partial(int , base=2)
# print(int2('1111111'))

# import functools

# max2 = functools.partial(max , 10)
# print(max2(1,5,2))

# import sys
# print(sys.path)

# class Students(object):

#     def __init__(self, name ,score):
#         self.name = name
#         self.score = score

#     def printStudent(self):
#         print("%s  %s " % (self.name  , self.score))
# bart = Students("bart" , 59)
# cy = Students("cy" ,100)
# bart.printStudent()
# cy.printStudent()

# class Students(object):

#     def __init__(self,name,score):
#         self.__name = name
#         self.__score = score
#     def __len__(self):
#         return 100
#     def getname(self):
#         return self.__name
#     def setname(self,name):
#         self.__name = name
# caiyi = Students("caiyi",100)
# print(caiyi.getname())

# print(dir(Students))
# caiyi = Students("caiyi",130)
# print(len(caiyi))

# class Students(object):
#     def set_name(self,name):
#         self.name = name
#     def print_name(self):
#         print(self.__name)
# caiyi = Students()
# caiyi.set_name("caiyi")
# print(caiyi.name)

# class Students(object):
#     __slots__ = ("name","age")
# caiyi = Students()
# caiyi.name = "caiyi"
# caiyi.age = 18
# caiyi.score = 100
# print(caiyi.name)

# class Students(object):

#     @property
#     def score(self):
#         return self.__score
    
#     @score.setter
#     def score(self,value):
#         self.__score = value
# s=Students()
# s.score = 60
# print(s.score)

# class Students(object):
#     def __init__(self, name, age):
#       self.name = name
#       self.age = age
#     def __str__(slef):
#         return "object name is %s" % slef.name
# s= Students("man",100)
# # print(Students("man",100))
# print(s)


# class Fib(object):
#     def __init__(self):
#         self.a = 0
#         self.b = 1
#     def __iter__(self):
#         return self
#     def __next__(slef):
#         slef.a , slef.b = slef.b , slef.a+slef.b
#         if slef.a > 1000:
#             raise StopIteration()
#         return slef.a
# for i in Fib():
#     print(i)

# class Fib(object):
#     def __getitem__(slef,n):
#         a , b = 1 , 1
#         for i in range(n):
#             a , b = b , a+b
#         return a
# f = Fib()
# print(f[10])

# class Students(object):
#     def __init__(self):
#         self.name = "caiyi"
#         self.age = 100
#     def __getattr__(self,attr):
#         if attr == "score":
#             return 100
# s =Students()
# print(s.score)

# from enum import Enum

# Month = Enum("Month",("Jan","Feb","Mar","Apr","May","Jun"))
# print(Month.Jan)
# for name, member in Month.__members__.items():
#     print(name, '=>', member, ',', member.value)
    

# from enum import Enum , unique

# @unique
# class Weekday (Enum):
#     Sun = 0
#     Mon = 1
# print(Weekday.Sun.value)

# import logging

# def foo(s):
#     return 10/int(s)
# def bar(s):
#     return foo(s)*2
# def main():
#     try:
#         bar("0")
#     except Exception as e :
#         logging.exception(e)
# main()
# print("END")

# i = 0 
# assert  i != 0
# print(i)

# import logging
# logging.basicConfig(level=logging.INFO)

# n = int(0)
# logging.info("n= %d" % n)
# print(10/n)

# from io import StringIO
# f = StringIO()
# f.write("hello")
# print(f.getvalue())

# from io import StringIO
# f = StringIO("Hello world")
# print(f.getvalue())
# while True:
#     s = f.readline()
#     if s == "":
#         break
#     print(s)

# from io import BytesIO
# f = BytesIO()
# f.write("中文".encode("utf-8"))
# print(f.getvalue())


# import os
# import os.path
# print(os.environ.get("PATH"))
# print(os.path.abspath("."))
# os.path.join("")

# import shutil
# shutil.copyfile

# import pickle
# d = {"name":"caiyi","age":20 , "score" :100}
# s = pickle.dumps(d)
# print(s)

# import json
# d = dict(name="caiyi",age=10,score=100)
# print(json.dumps(d))

import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))