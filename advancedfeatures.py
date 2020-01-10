# 切片
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print("切片原始数据L=", L)
# L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素
print("切片获取前几个值L[0:3]=", L[0:3])
print("切片获取前几个值L[1:3]=", L[1:3])
print("切片获取前几个值L[-2:-1]=", L[-2:-1])

# 迭代   dict就可以迭代：
d = {'a': 1, 'b': 2, 'c': 3}
print("迭代dict=", d)
for key in d:
    print("获取dict的key=", key)
    print("获取dict的value=", d[key])

for value in d.values():
    print(value)

for ch in 'ABC':
    print(ch)

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)

# 列表生成式
print(list(range(1, 11)))

L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])


# 生成器 odd不是普通函数，而是generator，在执行过程中，遇到yield就中断，下次又继续执行。执行3次yield后，已经没有yield可以执行了，所以，第4次调用next(o)就报错
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield (3)
    print('step 3')
    yield (5)


o = odd()
next(o)
next(o)
next(o)

# 迭代器
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
        print(x)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break
