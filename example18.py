#python函数
'''
函数代码块以def开头,后接函数标识名称和圆括号()

def 函数名(参数列表):
    函数体
'''
def area(width, height):
    return width * height
w, h = 4, 5
print('width=',w ,'height=',h, 'area=',area(w,h))


#可变类型:列表,字典;不可变类型:整数,字符串,元组
#python传不可变对象
def change(a):
    print(id(a))
    a = 10
    print(id(a))
a = 1
print(id(a))
change(a)

#python传可变对象
def changeme(list):
    list.append([1,2,3,4])
    print('函数内取值:', list)
    return
mylist = [10,20,30]
changeme(mylist)
print('函数外取值:', mylist)


#关键字参数
def printme(str):
    print(str)
    return
printme(str = '菜鸟教程')
'''
def printinfo(name, age):
    print('name:', name)
    print('age:', age)
    return
printinfo( age = 50, name = 'runoob')
'''


#不定长参数
def printinfo1(arg1, *vartuple):#加了*的参数以元组的形式存入，存放所以未命名的变量参数
    print('输出:')
    print(arg1,end=' ')
    print(vartuple)
printinfo1(20,88,'str')
def printinfo2(arg1, **vardict):#加了**的参数以字典的形式存入，存放所以未命名的变量参数
    print('输出:')
    print(arg1,end=' ')
    print(vardict)
printinfo2(20,a=1,b='str')

#声明函数时,参数中*可以单独出现,但其之后的参数必须用关键字传入
def f(a, b, *, c):
    return a+b+c
result = f(2,3,c=1)
print(result)


#匿名函数,用lambda创建，不再使用def语句这种标准定义一个函数，lambda只是一个表达式（语句）
x = lambda a : a + 10
print('a =',x(5))

sum = lambda arg1, arg2 : arg1 + arg2
print('相加后的值为:', sum(10,20))

def myfunc(n):
    return lambda a : a * n
mydoubler = myfunc(3)
print(mydoubler(22))


#return语句，用于退出函数


#强制位置参数
#函数形参语法/，用来指明形参必须使用指定位置参数，不能使用关键字参数的形式
def f1(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)
f1(10, 20, 30, d=40, e=50, f=60)
'''
f1(10, b=20, c=30, d=40, e=50, f=60)    b不能使用关键字参数的形式
f1(10, 20, 0, 40, 50, f=60)             e必须使用关键字参数的形式
'''