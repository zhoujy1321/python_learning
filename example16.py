#python循环语句
'''
while 判断条件(condition):
    执行语句(statements)...
'''
n = 100
sum = 0
counter = 1
while counter <= n:
    sum += counter
    counter+= 1
print('1到%d之和为:%d' % (n,sum))

#可以通过设置条件表达式永远不为false来实现无限循环
var = 1
while var == 1:
    num = int(input('输入一个数字,为0退出:'))
    print('你的输入为:',num)
    if(num == 0):
        break

print('______________________________')
#while循环使用else语句
'''
while condition:
    statements
else:
    addtional statements
'''
count = 0
while count < 5:
    print(count,'< 5')
    count += 1
else:
    print(count,'>= 5')

print('______________________________')
#for语句
'''
for <variable> in <variable>:
    <statement>
else:
    <statement>
'''
languages = ['C', 'C++', 'Java', 'Python']
for x in range(len(languages)):
    print(x,languages[x])

print('______________________________')
#range()函数,用于遍历数字序列
for i in range(0,9,3):
    print(i,end=',')
list1 = list(range(5))#用range()创建列表
print(list1)

for letter in 'runoob':
    if letter == 'b':
        break
    elif letter == 'n':
        pass
        print('execute pass mode')
        continue
    print('当前字母为:',letter)

#pass语句，为空语句，用作占位