#数据类型
#整数
a = 1;
print("整数",a);
#浮点数
b = 1.01;
print("浮点数",b);
#字符串
print("字符串","I\'m ok.");
#布尔值
print("布尔值",3>5);
#空值  是Python里一个特殊的值，用None表示。None不能理解为0，因为0是有意义的，而None是一个特殊的空值
print(None);
#常量 常量就是不能变的变量，比如常用的数学常数π就是一个常量。在Python中，通常用全部大写的变量名表示常量
PI = 3.14159265359;
print("常量",PI);
#计算
print(10 / 3);
print(9 / 3);
print(10 // 3);
print(10 % 3);
#字符编码
print(ord('A'));
print(chr(66));
print(len('ABC'));
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125));
print('中文'.encode('gb2312'));
#%d	整数
#%f	浮点数
#%s	字符串
#%x	十六进制整数

#******************-----------------***********************
#list,list是一种有序的集合，可以随时添加和删除其中的元素。
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates);
print(len(classmates));
print(classmates[0]);
#如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素
print(classmates[-1]);
classmates.append("hukaijia");
print(classmates);
print(len(classmates));
#插入数据
classmates.insert(0, 'Jack');
print(classmates);
#删除数据
classmates.pop();
print(classmates);
#tuple，tuple和list非常类似，但是tuple一旦初始化就不能修改，tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来
t = (1, 2);
print(t);
print(t[0]);

#if条件判断
age = 20
if age >= 18:
    print('your age is', age)
    print('adult')

age1 = 4
if age1>5:
    print("1111")
elif age1 == 4:
    print("3333333")

#for循环
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)
#range()函数，可以生成一个整数序列，再通过list()函数可以转换为list
print(list(range(5)))

#while循环
sum = 0
n = 99
while n>0:
    sum = sum + n
    n = n-2
print(sum)

#break的作用是提前结束循环

n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')

#continue语句，跳过当前的这次循环，直接开始下一次循环
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)

#dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储

d = {"a":"a","b":"b"}
print("dict示例",d["a"])
d["c"] = "c"
print("dict示例",d["c"])
print(d.get('Thomas'))
#要删除一个key，用pop(key)方法，对应的value也会从dict中删除
d.pop("c")
print("dict示例",d["c"])

