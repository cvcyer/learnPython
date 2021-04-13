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

>map 依次作用生成list    reduce  依次作用累积

`r = map(f,[1,2,3,4])`  map()函数，依次作用到list的每个元素。。接收两个参数，一个函数，一个iterable   生成的是一个Iterator

`list(r)`    将r转换为list， 是一个Iterable

~~~python
from functools import reduce
def add(x,y):
    return x+y
r = reduce(add,[1,2,3,4,5])
print(r)                          ##reduce使用方法，需要import
~~~

`reduce(f,[1,2,3,4])` reduce()函数将结果作用到下一个元素，最终累积。。。传入两个参数，一个函数，一个iterable。

>filter()过滤序列

~~~python
def is_odd(n):
    return n % 2 == 0
print(list(filter(is_odd,[1,2,3,4,5])))
~~~

`filter()`对list依次作用，true则保留，flase则遗弃。。接收两个参数，一个函数，一个list

~~~python
def odd_iter():
    n=1
    while True:
        n = n+2
        yield n
# odd_iter是一个生成器
def not_divisible(n):
    return lambda x: x%n > 0
def primes():
    yield 2
    it = odd_iter()
    while True:
        n = next(it)
        yield n 
        it = filter(not_divisible,it)
for i in primes():
    if i < 100:
        print(i)                          ## 生成100以内的素数
~~~

>排序函数

`sortd([1,2,3,4,5],key=abs，reverse=false)`  无key则默认按大小排序，按key排序,revers排序颠倒

>返回函数

把函数作为结果值返回

~~~python
def lazy_sum(*args):
    def sum():
        ex = 0
        for i in args:
            ex = ex + i
        return ex
    return sum
f = lazy_sum(1,2,3,4,5)
print(f)
print(f())
~~~

 f输出的是一个函数 f()调用才能真正计算

sum()使用外部函数的参数。返回sum，参数和变量都保存在sum函数中。这种称为`闭包`

 每次调用这个闭包函数时返回的函数不同

~~~python
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()                         ##f1() f2() f3()   =  9 9 9 
~~~

`f1()`并不是立即执行，而是等所有调用函数完成后再执行 ，所以9 9 9   。。 所以使用`闭包`时不要用任何循环

如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：

~~~python
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1,4):
        fs.append(f(i))
    return fs
for i in count():
    print (i())         ##保存到函数中，函数参数不会变。注意：这个list中都是函数
~~~

>匿名函数 lambda

`lambda x : x*x`  不需要return

>装饰器

代码运行期间动态增减功能的方式，称为`装饰器`  。 不需要改动函数本身

~~~python
def log(func):
    def wrappar(*args , **kw):
        print("call %s():" % func.__name__)
        return func(*args,**kw)
    return wrappar
@log
def now():
    print("打印一行")
print(now())
~~~

`@log` 相当于 log(now) 

~~~python
def log(text):
    def decorator(func):
        def wrapper(*args,**kw):
            print("%s %s:" % (text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator
@log("execute")
def now():
    print("2021/04/02")
now()                                   ##decorator本身带参数
~~~

`@log("exectue")`  相当于`now = log('execute')(now)`

~~~python
import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator                   ##一个完整带参数decorator写法
~~~

>偏函数

定义默认参数函数。偏函数可以简化

~~~python
import functools

int2 = functools.partial(int , base=2)
print(int2('1111111'))
~~~

实际上是把后边参数加到左边



>模块。 将函数封装到文件 。。。 一个个.py文件都是一个模块

每个模块的函数名和变量名都可以相同，不冲突

模块名有可能相同，引入`包` 来组织模块

目录下有`__init__.py`  则是一个包

>使用模块

模块的标准开头写法

~~~python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '               ##文档注释

__author__ = 'Michael Liao'     ##作者留名
~~~

`_name__`  特殊变量

`_private` 定义私有变量或私有函数

>安装第三方模块

Anaconda



>面向对象编程 OOP

面向对象在程序设计中更抽象

>类和实例

`class Students(object)` 定义类  object类是所有类的父类

`__init_(self,name,score) `  类的特殊方法,将属性绑定

>访问限制

数据封装：在类的内部定义访问数据的函数（即类的方法）

`self.__name = name`  将属性编程私有变量。 前面加双下划线

类中方法第一个参数都是self

>继承 

`class Dog(Animal)`

>多态

python作为动态语言的，具有鸭子类型的特性。 即不必严格继承，只需有相应的方法即可

>获取对象信息

`type(1)` 判断类型

`isinstance(h,dog)`  判断类的类型

`isinstance(1,int)` 判断数据类型

isinstance判断类型更全面

`dir("Students")`  输出类的所有属性和方法

~~~python
    def __len__(self):
        return 100
    caiyi = Students("caiyi",100)
    print(len(caiyi))       ##需要自己写一个len()方法，并实例化
~~~

>实例属性和类属性

`class Students(object):`

​			`name = "student"`

给类本身绑定属性，实例都能访问。但实例绑定相同，优先级更高





>面向对象高级编程

类绑定的方法，实例都能使用

>`__slots__` 约束类属性

`__slots_=("name","score")` 限制当前类的实例只能绑定相关属性>>只作用在本类，对子类不起作用

一般创建两个get set方法，实现对数据检查和封装。对外不可见。但比较繁琐

`@property`  装饰器可以让get set方法向属性访问一样简单

~~~python
class Students(object):

    @property
    def score(self):
        return self.__score
    
    @score.setter
    def score(self,value):
        self.__score = value
s=Students()
s.score = 60
print(s.score)
~~~

>多重继承

`class Dog(Animal , Runnable)`

这种多重继承的称为Mixln 混合类

>定制类

如 `__init_`  `__slots__` 均属于

`__str__(self)`  打印类其实是调用的此方法

`__iter__(self):          return slef`   迭代类本身

`__next__(self): `        `__next__(self)`方法拿到下一个值

~~~python

class Fib(object):
    def __init__(self):
        self.a = 0
        self.b = 1
    def __iter__(self):
        return self
    def __next__(slef):
        slef.a , slef.b = slef.b , slef.a+slef.b
        if slef.a > 1000:
            raise StopIteration()
        return slef.a
for i in Fib():
    print(i)                     ##类使用__iter__方法实现fib数列
~~~

`__getitem_()`将类表现为list，再将类实例化后，可以用下标访问

~~~python
class Fib(object):
    def __getitem__(slef,n):
        a , b = 1 , 1
        for i in range(n):
            a , b = b , a+b
        return a
f = Fib()
print(f[10])
~~~

`__getattr__(slef,attr)`  当调用的类属性`不存在时`会报错，此时会`自动`调用此方法寻找attr

~~~python
class Students(object):
    def __init__(self):
        self.name = "caiyi"
        self.age = 100
    def __getattr__(self,attr):
        if attr == "score":
            return 100
s =Students()
print(s.score)
~~~

`__call_(self)             caiyi()`    实例自身调用

>枚举类 enum

~~~python
from enum import Enum

Month = Enum("Month",("Jan","Feb","Mar","Apr","May","Jun"))
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)
~~~

生成了Month 类型的枚举类

或者继承Enum类实现

~~~python
from enum import Enum , unique

@unique
class Weekday (Enum):
    Sun = 0
    Mon = 1
print(Weekday.Sun.value)
~~~

>元类

type() 既能返回i对象类型，有可以动态创建

`metaclass` 动态创建类的同时，可以控制类的创建行为

高深



>错误、调试和测试

>错误

`try    except  finally`   try如果有错则不会执行try内语句，依次执行except finally(一定会执行)

错误也是类。所有错误都继承自`BaseException`，except捕获错误是会把捕获类的子类都一网打尽

`logging.execption(e)` 模块可以记录错误

`raise TypeError()`  抛出错误

还可以捕获到一个错误后抛出另一种类型的错误(要相关)

>调试

`print()`  简单粗暴，用后需要删除

`assert n != 0` 断言，如果n=0 后面程序不能运行，并抛出错误AssertionErrorr  `python -o test.py` 忽略断言

`logging`  允许记录信息级别

~~~python
import logging
logging.basicConfig(level=logging.INFO)

n = int(0)
logging.info("n= %d" % n)
print(10/n)
~~~

`python -m pdb test.py`  pdb调试，单步执行  n下一步   p i 查看变量 q退出调试

>单元测试

>文档测试



>I/O编程

同步I/O     异步I/O  是否等待

`with open(" " , "r") as f:        print(f.read())`    一次读出

`f = open(" ","rb")`        读取二进制文件

`f = open(" ","r",encoding = "gbk" ， errors = "ignore") `  读取特定编码，有错误时忽略

` with open(" " , "w") as f :   f.write(" ") `  写文件

w 有重复文件时会直接覆盖，  a 追加到文件末尾

>StringIO  和 BytesIO

在内存中读写字符串和byte

`from io import StringIO` 使用前需要导入这个包

`StringIO ` 只能操作str

`f =  StringIO("hello world")       f.readline()`

`BytesIO`  可以操作不同进制

~~~python
from io import BytesIO
f = BytesIO()
f.write("中文".encode("utf-8"))
print(f.getvalue())
~~~

>操作文件和目录

`import os`

`os.name` 查看操作系统类型

`os.uname()` 查看操作系统详细信息，win下没有

`os.environ`  查看系统环境变量

`os.environ.get("PATH")` 查看某个环境变量的值

操作文件和目录的函数一部分放在os中， 一部分放在os.path中

`print(os.path.abspath("."))`  查看当前文件的绝对路径

`os.path.join('/Users/michael', 'testdir')`   某个目录下创建新目录

`os.mkdir('/Users/michael/testdir')`  创建新目录

`os.rmdir('/Users/michael/testdir')`  删除目录

`os.path.split('/Users/michael/testdir/file.txt')`  拆分路径

`os.path.splitext()`  得到文件扩展名

shutil 模块提供os模块没有的功能，可以看作时补充

~~~python
import shutil

shutil.copyfile
~~~

 >序列化

将存储在内存的数据变为可传输或可存储 picking 其他语言叫seriallization

反序列化 unpicking

`pickle.dumps(d)` 对象序列化

`pickle.dump(d,f)` 对象序列化后写入文件

 `d = pickle.load(f)`  读序列化内容

> JSON

`import json`

`json.dumps(d)`  序列化 将dict类型转为json类型

`json.loads(json_str)` 反序列化 将str转为file_link_object

class 不能直接被json序列化，需要定义一个转换函数

~~~python
import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
        }
s = Student('Bob', 20, 88)
print(json.dumps(s, default=student2dict))
~~~

`Student`实例首先被`student2dict()`函数转换成`dict`，然后再被序列化为JSON：

`print(json.dumps(s, default=lambda obj: obj.__dict__))` 

也可以使用此方法直接转换。因为通常`class`的实例都有一个`__dict__`属性，它就是一个`dict`，用来存储实例变量。也有少数例外，比如定义了`__slots__`的class。

反序列化为一个class

~~~python
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
~~~





>进程和线程







>正则表达式

`\d`  匹配一个数字

`\w` 匹配一个字母或数字

`.` 匹配任意1个字符

` * `  匹配任意个任意字符

`+` 匹配至少一个字符

`?` 匹配0个或一个字符

`{n}` 匹配n个字符

`{n,m}` 匹配n-m个字符

`\` 匹配特殊字符转义

exm: `\d{3}\s+\d{3,8}}`  匹配三个数字，0个或一个空格或tab，匹配3到8个数字 123 12345

exm: 匹配010-12345  `\d{3}\-\d{3,8}`

`[ ]` 表示范围

​	`[0-9a-zA-Z\_]` 匹配一个数字 字母 或下划线

​	`[0-9a-zA-Z\_]+` 匹配至少一个数字，母或下划线组成的字符串

`A|B` 匹配A或B

`^` 行开头  `^\d` 必须以数字开头

`$` 行结尾 `\d$` 必须以数字结尾



`import re`  py中正则表达式模块

`r'abc'` 对字符串不专一

`re.match("正则",字符串)` 判断是否匹配，匹配成功返回一个对象，不成功返回none

```
>>> re.split(r'[\s\,\;]+', 'a,b;; c  d')
['a', 'b', 'c', 'd']
```

```
>>> m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
>>> m.group(0)
'010-12345'
>>> m.group(1)
'010'
>>> m.group(2)
'12345'
```

`()` 提取保存组

`group(0)` 原字符串

`groups()` 列出匹配出的组

正则默认贪婪匹配

`?` 使用非贪婪匹配

```
>>> re.match(r'^(\d+?)(0*)$', '102300').groups()
('1023', '00')
```

预编译正则表达式

```
>>> import re
# 编译:
>>> re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
# 使用：
>>> re_telephone.match('010-12345').groups()
('010', '12345')
>>> re_telephone.match('010-8086').groups()
('010', '8086')
```



>常用内置模块

>datetime  时间模块

`from datetime import datetime`

`datetime.now()` 获取当前时间

`datetime(2021,4,9,10,19)` 指定时间

`dt.timestamp()` 转换为时间戳

`datetime.formtimestamp(t)` 将t时间戳转换为时间

`cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S') `        格式化字符串为时间

`print(now.strftime('%a, %b %d %H:%M'))`   格式化字符时间格式

`from datetime import datetime, timedelta`  对时间进行加减

```
>>> now + timedelta(days=2, hours=12)
datetime.datetime(2015, 5, 21, 4, 57, 3, 540997)
```

本地时间转换为UTC时间

时区转换

>collections  内建集合模块

namedtuple 不变集合

~~~python
from collections import namedtuple
Point = namedtuple("Point",["x","y"])
p=Point(1,2)
print(p.x)
print(p.y)                    ##表示二维坐标
~~~

deque 解决list插入不方便

```
>>> from collections import deque
>>> q = deque(['a', 'b', 'c'])
>>> q.append('x')
>>> q.appendleft('y')
```

`appendleft()`和`popleft()`

defaultdict  引用key不存在返回默认值

```python
from collections import defaultdict
dd = defaultdict(lambda: 'N/A')
 dd['key2'] # key2不存在，返回默认值
```

OrderedDict 使dict有序

```
>>> from collections import OrderedDict
>>> d = dict([('a', 1), ('b', 2), ('c', 3)])
>>> d # dict的Key是无序的
{'a': 1, 'c': 3, 'b': 2}
>>> od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
>>> od # OrderedDict的Key是有序的
OrderedDict([('a', 1), ('b', 2), ('c', 3)])
```

key是按照插入的顺序排列

`OrderedDict`可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key：

ChinaMap  将多个dict串起来

```python
from collections import ChainMap
combined = ChainMap(command_line_args, os.environ, defaults)
```

Counter 计数器，统计字符在字符中出现次数

```python
>>> from collections import Counter
>>> c = Counter()
>>> for ch in 'programming':
...     c[ch] = c[ch] + 1
...
```

>base64  二进制转换为字符

`import base64`

` base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')      b'abcd++//'`             

```python
>>> base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
b'abcd--__'
>>> base64.urlsafe_b64decode('abcd--__')
b'i\xb7\x1d\xfb\xef\xff'                     
```

urlsafe_b64会把 +  / 变为   -  _     上面为urlsafe的编解码

Base64编码后会自动把`=`忽略

>struct  bytes与二进制数据类型转换

~~~python
import struct
s =struct.pack(">I",2111)
~~~

`>I` >表示字节顺序 big-endian 网络序   I 表示4字节无符号整数

`>IH` I 4 字节无符号整数， H 2字节无符号整数

bmp位图

```
>>> struct.unpack('<ccIIIIIIHH', s)
(b'B', b'M', 691256, 0, 54, 40, 640, 360, 1, 24)
```

`b'B'`、`b'M'`说明是Windows位图，位图大小为640x360，颜色数为24。

两个字节：`'BM'`表示Windows位图，`'BA'`表示OS/2位图； 一个4字节整数：表示位图大小； 一个4字节整数：保留位，始终为0； 一个4字节整数：实际图像的偏移量； 一个4字节整数：Header的字节数； 一个4字节整数：图像宽度； 一个4字节整数：图像高度； 一个2字节整数：始终为1； 一个2字节整数：颜色数。

>hashlib  提供常见摘要算法（哈希，散列）

~~~python
import hashlib

md5 = hashlib.md5()
md5.update('caiyi666'.encode("utf-8"))
print(md5.hexdigest())
~~~

md5 任意字符串转换为32位(128bit)

```python
import hashlib

sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())
```

sha1  160bit

常见密码可以加slat来使其得到不同md5



>hmac     通过一个标准算法，将key混入其中

```
>>> import hmac
>>> message = b'Hello, world!'
>>> key = b'secret'
>>> h = hmac.new(key, message, digestmod='MD5')
>>> h.hexdigest()
'fa4ee7d173f2d97ee79022d1a7355bcf'
```

>itertools  用于操作迭代对象

```
>>> import itertools
>>> natuals = itertools.count(1)
>>> for n in natuals:
...     print(n)
```

`count(1)`从1开始无限循环

`cycle("abc")`  无限循环输出abc

`repeat("a",3)`  输出3次a

`ns = itertools.takewhile(lambda x: x <= 10, natuals)`    takewhile()  给定结束条件

>contextlib    `open with` 其实是实现了上下文管理

~~~python
from contextlib import contextmanager

@contextmanager
def tag():
with tag()    
 
~~~

contextlib 可以实现我们某段代码前自动执行某段代码

>closing    一个对象未实现上下文，可以用closing()将这个对象变为上下文对象

~~~python
from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('https://www.baidu.com')) as page:
    for line in page:
        print(line)
~~~



>urllib  对URL进行操作

>Get   requetst模块发送Get请求到页面，返回http响应