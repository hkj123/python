try:
    f = open('D:/python/test.txt', 'r')
    print(f.read())
finally:
    if f:
        f.close()

#Python引入了with语句来自动帮我们调用close()方法
with open('D:/python/test.txt', 'r') as f:
    print("with open 方法",f.read())
#前面的try ... finally是一样的，但是代码更佳简洁，并且不必调用f.close()方法

# f = open('D:/python/test.txt', 'w')
# f.write('Hello, world!')
# f.close()
#
# with open('D:/python/test.txt', 'w') as f:
#     f.write('Hello, world!')

#StringIO就是在内存中创建的file-like Object，常用作临时缓冲
#StringIO顾名思义就是在内存中读写str
from io import StringIO

f = StringIO()
f.write('hello hu kai jia')
print(f.getvalue())

#BytesIO
from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())

#操作文件和目录
import os
print(os.name)
#如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统
print(os.environ)

#序列化
import pickle
d = dict(name='Bob', age=20, score=88)
print(pickle.dumps(d))

#JSON

# JSON类型	     Python类型
# {}	         dict
# []	         list
# "string"	      str
# 1234.56	      int或float
# true/false	   True/False
# null	           None

import json
d = dict(name='Bob', age=20, score=88)
print(json.dumps(d))
#dumps()方法返回一个str，内容就是标准的JSON。类似的，dump()方法可以直接把JSON写入一个file-like Object
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str))

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 26, 88)
#可选参数default就是把任意一个对象变成一个可序列为JSON的对象，我们只需要为Student专门写一个转换函数，再把函数传进去即可：
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }
jn = json.dumps(s, default=student2dict)
print("python类转换成json",jn)

def dict2student(d):
    return Student(d['name'], d['age'], d['score'])
s = json.loads(jn, object_hook=dict2student)
print("json转换成python类",s)
print(s.name)
















