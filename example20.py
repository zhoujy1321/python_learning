#python模块
import sys  #引入sys.py模块
import fibo

print('命令行参数如下:')
for i in sys.argv:  #sys.argv是一个包含命令行参数的列表
    print(i)
print('\n\nPython路径为:',sys.path,'\n')    #sys.argv包含了一个python解释器自动查找所需模块的路径的列表

fibo.fib(1000)
res = fibo.fib2(100)
print(res)



#from ... import语句，从模块中导入一个指定的部分
#from fibo import fib, fib2


#深入模块


#__name__属性


#dir()函数，可以找到模块内定义的所有名称


#标准模块


#包


