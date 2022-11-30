
#多行语句只需用一个\即可，在括号(){}[]内不需要使用\

#数字类型有int,bool,float,complex
str = '123456789'
print(str)
print(str[0:-1])#输出从第一个到倒数第二个字符
print(str[0])
print(str[6:8])
print(str[2:])
print(str[1:5:2])
print(str*2)
print(str + '您好')
print('------------------')
print('hello\nrunnob')
print(r'hellp\nrunnob')#字符串前面加一个r，表示原始字符串，不会转义
#python没有单独的字符类型，不能对字符串里面的单个位置进行赋值，这点和C不一样

#输入
sign = input('\n按输入1后输出一个换行,否则退出')
if sign == 1:
    print('\n')
else:
    print('quit.')

#print输出默认换行，实现不换行需要在变量末尾加上end=""
x = 'a'
y = 'c'
print(x)
print(y)#换行输出
print( x,end=" ")
print( y,end=' ')

#python中用import来导入相应的模块
