>**Base**

Cpython 官方解释器

IPython 交互式解释器，交互上有增强

PyPy 动态解释器，可以提高执行速度，但和CPython稍有不同

JPython 可以把python代码编译为class字节码

IronPython  可以编译成.NET字节码

`0x` 16  进制

`\` 转义字符

`r' '` 空格之间的字符不专一

`'''line1...line2...line3'''`  ‘’‘ ...''' 表示多行内容

`True  False` 布尔值 

`and  or  not `   与  、 或 、 非 

`None` 空值

`ord()`  获取字符的ASCII 

`chr()`  把编码转换为字符

`b'ABC'` 将字符串转为byte类型   `只有byte类型的编码才可以在网络上传输，或保存到磁盘里`

`.decode()` 将byte转换为特定编码

`.decode('utf-8',errors='ignore')`  忽略编码方式无法识别的字节

`len()` 计算字符数

`#!/usr/bin/env python3   # -*- coding: utf-8 -*-` 通常子啊python文件前加此段让其按照utf-8编码读取

`"hello , %s . you have %d money" % ('caiyi',10000000000000000)`  字符格式化，%s字符串 ，%d 整数    `%s` 会把任何数据类型转换为字符串

`%%` 转义%

`"hello ,{0} . you  tall {1:.1f} m " .format('caiyi',1)` format方法格式化字符

`print(f"{r}{s:.2f}")` f-string 方法格式化字符串



> list 列表 []

`list = [ ]`

`len()` 获取list元素个数

`list[0]  list[1]`  索引访问

`list[-1]` 最后一个元素

`list.append(" ")` 追加元素到末尾

`list.insert(1," ")` 插入元素到指定index ，依次后移

`list.pop()` 删除末尾元素

`list.pop(1)` 删除指定index元素

`list.sort()` 元素排序 

`list[1]=" "` 指定index元素替换

list元素数据类型可以不同

list 可以是二维及以上

>tuple  元组 ()

tuple 元组一旦确定，不可更改

`tuple = ( )`

 `tuple = (1,)` 定义只有一个元素的tuple元组，元素后必须加， 不然会认为是一个数

 `tupel = (1,2,["caiyi","ccyy"])` 元组不可变指指向不变，如果里面元素为变量，则可以发生改变

>dict 字典  {}  即key-value键值对 。>查找迅速，但内存耗费少 

~~~python
d = {"caiyi":98,"cc":99}
print(d["caiyi"])                ##注意是{}花括号
~~~

`d["ccyy"] = 100 `  加入新记录

键不存在，会报错

`d.get("ccyy",0)` 不存在则返回0

`d.pop("cc")` 删除一个map

`key不能变。所以list不能作为dict的键`

>set集合 ([])  无序且不重复

set集合参数为一个固定不变list

`s = set ([1,2,3,4])`

`s.add(8)` 添加参数

`s.remove(8)` 删除参数

`s1 & s2`  交

`s1 | s2` 并





>条件判断  if: elif: else: 

~~~python
if age >= 18 :
    print("you age is" , age )
elif age >=6:
    print("teenager")
else:
    print("no have age")
~~~

~~~python
if 1:
    print("")         ##永真判断
~~~

`int()` 将字符串类型转换为int型

>循环

`for in` 循环迭代每一个元素

~~~python
names = ["caiy" , "cay" ,"cyyy"]
for name in names:
    print(name)                     ##循环迭代list每一个元素
~~~

~~~python
for i in range(101):
    print(i)                ##生成0-100的数
~~~

`while  ：`  while条件判断循环

`break ` 提前结束循环

`continue`  跳过当前循环





>函数

py内置函数

`abs()` 求绝对值

`max()` 求最大值

`int()` 其他类型转换为整数类型

`a = abs  a(-1)` 函数名指向

`hex()` 转换为十六进制

`def  :` 定义函数

`pass` 什么也不做做占位

`raise TypeError(" ")` 自定义输入错误

`return x ,y ` python函数允许多个返回值  ——其实返回的一个tuple，一一对应并且没括号

>默认参数

`def power(x,n=2):`  n默认参数为2    变化大的放前面，变化小的放后面。。。默认参数必须指向不变对象。。 ----比如list，为可变对象，每次调用都会记住之前的

`def add_end(L=None):` 正确的list传入方法  `def add_end(L=[])`错误 

>可变参数 *nums

`def calc(*nums):` nums作为一个可变参数传入

~~~python
def calc (*nums) :
    sum = 0
    for n in nums:
        sum = sum + n*n
    return sum
print(calc(1,2,3))
~~~

>关键字参数 **other

`def person(name,age,**other):`  **参数会获取一个dict作为参数

~~~python
def person (name,age,**kw):
    print("name:",name,"age:",age,"other:",kw)
person("才艺",18,city="beijing",country="china")
~~~

>命名关键字参数  ` , * , , ,` *号后的作为关键字参数，只接受他们

~~~python
def person (name,age,*,country,sex):
    print("name:",name,"age:",age,"country:",country,"sex:",sex)
person("caiyi",18,country="china",sex="gg")        ##必须指定
~~~

如果参数中已经有可变参数*nums ，则不需要再跟 星号了，后面默认为命名关键字参数

命名关键字参数也可以缺省

在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

>递归函数

函数内部调用自身

~~~python
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
print(fact(5))
~~~

递归函数需要防止栈溢出 ： 每进入一个函数调用，加一层栈帧

>尾递归

循环是一种特殊的尾递归函数

尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。

~~~python
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
~~~

尾递归调用时，如果做了优化，栈不会增长，因此，无论多少次调用也不会导致栈溢出。

遗憾的是，大多数编程语言没有针对尾递归做优化，Python解释器也没有做优化，所以，即使把上面的`fact(n)`函数改成尾递归方式，也会导致栈溢出。



>高级特性



>切片

`L[0:3]` 取前三个元素 0 1 2

`L[:3]` 如果从第0个元素开始，可省略0

`L[-2:-1]` 最后一个元素为-1 

`L[0:10:3]` 每三个取一个 0  3 6 9

`print("today is fine"[::2])`  字符串也可以取

>迭代

字典默认迭代key  ， 如果要迭代value `dic.values()` ,  如果要迭代key , values `dic.items()`

~~~python
from collections import Iterable
isinstance (dic,Iterable)                 ##判断对象是否可迭代
~~~

`for i , v in enumerate(list)` 实现下标迭代 0 ，"ccyy" 

 >列表生成式

`list = [ x * x for x in range(1,11)]`      生成1*1类型list

`list = [x*x for x in range(1,11) if x%2 == 0]`  列表生成并加上if语句  if后不能加else，if只是一个过滤条件

`list = [m+n for m in "abc" for n in "def"]`  两层循环生成

`os.listdir()`   os模块列出文件和目录

>生成器

一次性生成列表会占用大量内存，可以在循环过程中不断推算后续元素。这样动态生成称为生成器

`list = [x*x for x in range(1,100)]` 生成式方式

`g = (x*x for x in range(1,100))`  生成器方式    `next(g)` 打印g的下一个元素

~~~python
g = (x*x for x in range(1,111111))
for i in g:
    print(i)                           ##生成器方式生成的遍历
~~~

~~~python
#斐波拉契数列  1 1 2 3 5 8 13
def fib(max):
    n , a , b = 0 , 0 ,1
    while n < max:
        print(b)
        a , b = b , a+b
        n=n+1
    return 'completed'
print(fib(10))                          ##循环方式生成数列
~~~

`print(b)  改为 yield(b) `   普通函数改为生成器

~~~python
def fib(max):
    n , a , b = 0 , 0 ,1
    while n < max:
        yield b
        a , b = b , a+b
        n=n+1
    return 'completed'
for i in fib(10):
    print(i)                                ##生成器方式生成fib数列
~~~

生成器是在yield时中断。继续执行下面，最终函数变为生成器。for in 方式打印生成器内容

即实际生成了一个gen对象

>迭代器

可以用for循环的对象称为 可迭代对象 Iterable

~~~python
from collections.abc import Iterable
print(isinstance(fib,Iterable))                 ##判断是否为可迭代对象
~~~

可以被next()函数调用的称为迭代器

~~~python
from collections.abc import Iterator
print(isinstance(fib,Iterator))                  ##判断是否为迭代器
~~~

迭代器是惰性的，只有调用它，他才会计算。。 所以可以表示无限大



>函数式编程

纯粹的函数式编程没有变量，输入确定，输出一定确定。。。 称为无副作用

特点：允许把函数作为参数传入另一个函数，还允许返回函数

>高阶函数

`f = abs   f(-10)` 函数赋给变量

函数接收另一个函数作为参数称为`高阶变量`