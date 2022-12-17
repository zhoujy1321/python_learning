#python输入和输出
'''
两种输出值的方式:表达式语句,print()函数
第三种是使用文件对象的write()方法,标准输出文件可以用sys.stdout引用
str.format()函数格式化输出值
str():返回一个用户易读的表达形式,repr():产生一个解释器易读的表达形式
'''
import math

#旧式字符串格式化
print('常量Pi的值近似为: %5.6f。' % math.pi)


#读取键盘输入input()函数
str = input('请输入:')
print('你输入的内容是:', str)


#读和写文件

#文件对象的方法
'''
f.read():读取一定数目的数据,然后作为字符串或字节对象返回
f.readline():从文件中读取单独的一行,换行符为'\n',返回空字符串时读取到最后一行
f.readlines():返回文件中包含的所有行
f.write(str):将str写入到文件中,然后返回写入的字符数
f.tell():返回文件对象当前所处的位置
f.seek(offset,from_what):改变文件指针的位置
f.close()
'''


#pickle模块,实现基本的数据序列和反序列化