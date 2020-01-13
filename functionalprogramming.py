# 高阶函数英文叫Higher-order function
# Python内建了map()和reduce()函数
# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
def f(x):
    return x * x
r = map(f, [1, 2, 3, 4, 5, 6])
print(list(r))
# map()传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list
L = []
for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    L.append(f(n))
print(L)
# map() 会根据提供的函数对指定序列做映射。
# map(function, iterable, ...)
# Python 3.x 返回迭代器。
# print(map()) 返回迭代器地址
# 一般和list一起用 才能输出
# reduce() 函数会对参数序列中元素进行累积。先对集合中的第 1、2 个元素进行操作，得到的结果再与第三个数据用 function 函数运算，最后得到一个结果。
# reduce(function, iterable[, initializer])
from functools import reduce
def add(x, y):
    return x + y
count = reduce(add, [1, 2, 3, 4, 5])
print(count)
# 计算列表和：1+2+3+4+5
#filter()函数用于过滤序列
def not_empty(s):
    return s and s.strip()
print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))
# 排序算法  sorted
print(sorted([36, 5, -12, 9, -21]))
print(sorted([36, 5, -12, 9, -21], key=abs))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0]
L1 = sorted(L, key=by_name)
print(L1)
def by_score(t):
    return t[1]
L2 = sorted(L, key=by_score,reverse=True)
print(L2)

#返回函数

#匿名函数 匿名函数有个好处，因为函数没有名字，不必担心函数名冲突   匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果
print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

#装饰器 在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）

#简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单
import functools
int2 = functools.partial(int, base=2)
print(int2('1000000'))