#python条件控制
'''
if condition1:
    statement1
elif condition2:
    statement2
else:
    statement3
'''

var1 = 100
if var1:
    print('1-if表达式条件为true')
    print(var1)
var2 = 0
if var2:
    print('2-if表达式条件为true')
    print(var2)

age = int(input('输入你家狗狗的年龄:'))
print("")
if age <= 0:
    print('are u kidding me?')
elif age == 1:
    print('is similar to 14 years old person')
elif age == 2:
    print('is similar to 22 years old person')
elif age > 2:
    human = 22 + (age - 2)*5
    print('对应人类年龄:',human)
input('点击enter退出')


#match...case(python3.10增加)
def http_error(status):
    match status:
        case 400:
            return 'Bad request'
        case 404:
            return 'Not found'
        case 418:
            return 'I\'m a yeapot'
        case _:
            return 'sth\'s wrong with the internet'
mystatus = 400
print(http_error(400))