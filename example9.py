#python字符串
var1 = 'Hello World!'
var2 = "Runoob"
 
print ("var1[0]: ", var1[0])
print ("var2[1:5]: ", var2[1:5])

#字符串更新
print('已更新字符串：',var1[:5]+'runoob')
print('已更新字符串：',var1[:6]+'runoob')

#转义字符
print('\a')
'''
\\   \'   \"   \b   \000(空)   \n(换行)   \v(纵向制表符)   \t(横向制表符)
'''

#字符串运算符
a = "Hello"
b = "Python"
 
print("a + b 输出结果：", a + b)
print("a * 2 输出结果：", a * 2)
print("a[1] 输出结果：", a[1])
print("a[1:4] 输出结果：", a[1:4])
 
if( "H" in a) :
    print("H 在变量 a 中")
else :
    print("H 不在变量 a 中")
 
if( "M" not in a) :
    print("M 不在变量 a 中")
else :
    print("M 在变量 a 中")
 
print (r'\n')
print (R'\n')

#字符串格式化
print ("我叫 %s 今年 %d 岁!" % ('小明', 10))

#三引号
para_str = """这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )。
也可以使用换行符 [ \n ]。
"""
print (para_str)

#f-string
#f-string 格式化字符串以 f 开头，后面跟着字符串，字符串中的表达式用大括号 {} 包起来，它会将变量或表达式计算后的值替换进去
w = {'name': 'Runoob', 'url': 'www.runoob.com'}
print(f'{w["name"]}: {w["url"]}')

x = 1
print(f'{x+1}')   
print(f'{x+1=}')   

#字符串内建函数
'''
.................
'''