#Student类为例，在Python中，定义类是通过class关键字：
class Student(object):
    pass
bart = Student()

print(bart)
print(Student)
bart.name = 'Bart Simpson'
print(bart.name)

#__init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身
class Student1(object):

    def __init__(self,name,score):
        self.name = name
        self.score = score

#在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不需要传，Python解释器自己会把实例变量传进去
bart1 = Student1("hukaijia",100)
print(bart1.name)
print(bart1.score)

def print_score(std):
    print('%s: %s' % (std.name, std.score))

print_score(bart1)

#Student实例本身就拥有这些数据，要访问这些数据，就没有必要从外面的函数去访问，可以直接在Student类的内部定义访问数据的函数，这样，就把“数据”给封装起来了。这些封装数据的函数是和Student类本身是关联起来的，我们称之为类的方法

class Student2(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

bart2 = Student2("hukaijia3",1003)
bart2.print_score()
print(bart2.get_grade())

#如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问，所以，我们把Student类改一改：
class Student3(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    # def get_name(self):
    #     return self.__name
    #
    # def get_score(self):
    #     return self.__score
    #
    # def print_score(self):
    #     print('%s: %s' % (self.__name, self.__score))

bart3 = Student3("hukaijia4",1004)
# print(bart3.get_name())
# # bart3.print_score()

class Animal(object):
    def run(self):
        print("Animal is running...")

#当我们需要编写Dog和Cat类时，就可以直接从Animal类继承

class Dog(Animal):
    pass

class Cat(Animal):
    pass

dog = Dog()
dog.run()

class Dog1(Animal):

    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')

dog1 = Dog1()
dog1.run()

a = list() # a是list类型
b = Animal() # b是Animal类型
c = Dog() # c是Dog类型

print(isinstance(a, list))
print(isinstance(b, Animal))
print(isinstance(c, Dog))

def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Dog1())

#获取对象信息
#使用type()  判断对象类型，使用type()函数
print("type()",type(123))

#isinstance()  class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数
print("isinstance()",isinstance(b, Animal))

#dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法
print(dir('ABC'))
