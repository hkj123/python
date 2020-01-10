# 调用abs函数
print(abs(-100))
print("调用abs函数", abs(-100.01))
# 调用max函数
print("调用max函数", max(1, 2, 3, 4, 5))
# 调用int()函数
print("调用int()函数", int(12.34))
# 调用float函数
print("调用float函数", float('12'))


# 定义函数
def my_function(x):
    if x > 0:
        return "大于0"
    else:
        return "小于0"


print("调用自己定义的函数", my_function(10))


# 定义空函数 pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass
def nop(age):
    if age >= 18:
        pass


# 返回多个值
def return_twovalue(x, y):
    return x, y


a, b = return_twovalue(1, 2)
print("返回多个值", a, b)


# 递归函数
def digui(x):
    if x == 1:
        return 1
    return x * digui(x - 1)


print("递归函数返回", digui(10))
