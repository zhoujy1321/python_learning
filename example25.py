#python面向对象
'''
类:定义集合中每个对象所共有的属性和方法
方法:类中定义的函数
类变量:定义在类中且函数体之外
数据成员:类变量或实例变量用于处理类及其实例对象相关的数据
方法重写:
局部变量:定义在方法中的变量
实例变量:在类的声明中,属性用变量表示,这种变量为实例变量
继承:
实例化:
对象:通过类定义的数据结构实例,包括两个数据成员(类变量和实例变量)和方法


类定义格式:
class classname:
    <statement1>
    ...
    ...
    <statementN>
创建一个之后,可以通过类名访问其属性
'''
#类对象:支持两种操作,属性引用和实例化
class Myclass:
    i = 12345
    def f(self):
        return 'hello world'
x = Myclass()
print('Myclass类的属性 i 为:',x.i)
print('Myclass类的方法 f 输出为:',x.f())

class complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
x = complex(3.0,-4.5)
print(x.r, x.i)


#self代表类的实例,而非类
class test:
    def prt(self):
        print(self)
        print(self.__class__)
t = test()
t.prt()#self代表类的实例,代表当前对象的地址,self.class指向类



#类的方法
class people:
    name = ''   #定义基本属性
    age = 0
    __weight = 0    #定义私有属性.私有属性在类外部无法直接访问
    def __init__(self,n,a,w):   #定义构造方法
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print('%s 说：我 %d 岁，体重 %d 千克。' %(self.name, self.age, self.__weight))
p = people('runoob', 10, 50)
p.speak()



#类的继承
'''
class DerivedClassName(BaseClassName):
    <statement-1>
    ...
    <statement-N>
'''
class student(people):  #单继承
    grade = ''
    def __init__(self,n,a,w,g):
        people.__init__(self,n,a,w) #调用父类的构函
        self.grade = g
    def speak(self):
        print('%s 说：我 %d 岁，我在读 %d 年级。' %(self.name, self.age, self.grade))
s = student('Eric', 10, 60, 3)
s.speak()


#多继承
'''
class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    ...
    <statement-N>
'''
class speaker():
    topic = ''
    name = ''
    def __init__(self,n,t):
        self.name = n
        self.topic = t
    def speak(self):
        print('我系 %s,我系一个吹牛逼的,我今天的话题系 %s。' % (self.name, self.topic))
class sample(speaker,student):
    a = ''
    def __init__(self,n,a,w,g,t):
        student.__init__(self,n,a,w,g)
        speaker.__init__(self,n,t)
test = sample('Tim', 25, 80, 4, 'python')
test.speak()



#方法重写
class Parent:   #定义父类
    def mymethod(self):
        print('调用父类方法')
class Child(Parent):    #定义子类
    def mymethod(self):
        print('调用子类方法')
c = Child()
c.mymethod()    #子类调用重写方法
super(Child,c).mymethod()   #用子类对象调用父类已经被覆盖的方法






#类属性与方法
'''
类的私有属性:__private_attrs,两个下划线开头,声明该属性为私有,不能在类的外部被使用或直接访问,在内部使用时self.__private_attrs.
类的方法:在类的内部,使用def定义一个方法,类方法必须包含参数self,且为第一个参数,self代表类的实例
类的私有方法:__private_method,两个下划线开头,声明该方法为私有方法,只能在类的内部调用self.__private_method
'''
class Justcounter:      #类的私有属性
    __secretcount = 0   #私有变量
    publiccount = 0     #公开变量
    def count(self):
        self.__secretcount += 1
        self.publiccount += 1
        print(self.__secretcount)
counter = Justcounter()
counter.count()
counter.count()
print(counter.publiccount)
#print(counter.__secretcount)   #私有变量不能访问

class Site:     #类的私有方法
    def __init__(self, name, url):
        self.name = name
        self.__url = url
    def who(self):
        print('name:', self.name)
        print('url', self.__url)
    def __foo(self):                #私有方法
        print('你到了私有方法！')
    def foo(self):                  #公共方法
        print('你到了公共方法！')
        self.__foo()
x = Site('菜鸟教程', 'www.runoob.com')
x.who()
x.foo()
#x.__foo()      #私有方法不能访问

'''
类的专有方法:
__init__:构造函数,在生产对象时调用
__del__:析构函数,释放对象时使用
__repr__:打印,转换
__setitem__:按照索引赋值
__getitem__:按照索引获取值
__len__
__cmp__:比较
__call__:函数调用
__add__
__sub__
__mul__
__truediv__
__mod__
__pow__
'''


#运算符重载
class vector:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __str__(self):
        return 'vector (%d %d)' % (self.a, self.b)
    def __add__(self,other):
        return vector(self.a + other.a, self.b + other.b)
v1 = vector(2,10)
v2 = vector(5,-2)
print(v1 + v2)