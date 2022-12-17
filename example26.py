#python命名空间和作用域
#命名空间


#作用域


#全局变量和局部变量


#global和nonlocal关键字
num = 1
def fun1():
    global num  #修改全局变量num
    print(num)
    num = 123
    print(num)
fun1()
print(num)
def outer():
    num = 10
    def inner():
        nonlocal num    #nonlocal修改嵌套作用域中的变量
        num = 100
        print(num)
    inner()
    print(num)
outer()