#!/usr/bin/env python
# -*- coding : utf-8 -*-
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

def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
print(fact(1000))