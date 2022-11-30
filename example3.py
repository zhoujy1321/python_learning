counter = 100
miles = 100.0
name = 'runoob'
print(counter)
print(miles)
print(name)

#多变量赋值
a = b = c = 1
d,e,f = 1,2,'runoob'
print(a,b,c,d,e,f)

#python有六个标准的数据类型：number,string,list(unchangeble),tuple,set,dictionary(changeble)
#可以用del语句删除一些对象引用
#乘法*，除法：/（浮点数），//（整数），取余%，乘方**
#复数：a+bj or complex(a,b)



print('列表：-------------------------\n')
#列表(List)：是在【】之内，用逗号分隔开的元素列表
list = ['abcd',786,2.23,'runoob',70.2]
tinylist = [123,'runoob']
print(list)
print(list[0])
print(list[1:3])#从第二个元素开始输出到第三个元素
print(list[2:])
print(tinylist*2)
print(list + tinylist)

#列表的元素可以改变，和字符串不一样
a = [1, 2, 3, 4, 5, 6]
print(a)
a[0] = 9
a[3:5] = [8, 7]#改变第四个到第五个
print(a)

#翻转字符串样例
def reversewords(input):
    inputwords = input.split(" ")
    inputwords = inputwords[-1: :-1]
    output = ' '.join(inputwords)
    return output
if __name__ == "__main__":
    input = 'i like runoob'
    rw = reversewords(input)
    print(rw)



print('元组：-------------------------\n')
#元组(Tuple)：和列表类似，和列表相比，元素用()括起来，且元素中的元素不能修改
tuple = ('abcd',786,2.23,'runoob',70.2)
tinytuple = (123,'runoob')
print(tuple)
print(tuple[0])
print(tuple[1:3])#从第二个元素开始输出到第三个元素
print(tuple[2:])
print(tinytuple*2)
print(tuple + tinytuple)
#可将列表看成特殊的元组
#特殊元组
tup1 = ()#空元组
tup2 = (10,)#一个元素，需要在元素后添加逗号



print('集合：-------------------------\n')
#集合(set)：进行成员关系的测试和删除重复元素，可使用大括号{}或者set()函数创建集合
sites = {'google','taobao','baidu','facebook','twitter','insgram'}
#成员测试
if 'twitter' in sites:
    print('twitter在集合中')
else:
    print('twitter不在集合中')
#set可以进行集合运算
h = set('qwertyuiop')
i = set('qwerty')
print(h)
print(h - i)#差集
print(h | i)#并集
print(h & i)#交集
print(h ^ i)#不同时存在的元素   




print('字典：-------------------------\n')
#字典(dictionary):无序的对象集合，列表是有序的对象集合，字典中元素是通过键来存取的，不是通过偏移存取；
#用{}标识，是一个键(key):值(value)的集合
dict = {}#空字典
dict['one'] = "1 - 菜鸟教程"
dict[2] = "2 - 菜鸟工具"
tinydict = {'name':'runoob', 'code':1, 'web':'www.runoob.com'}
print(dict['one'])#输出键为'one'的值
print(dict[2])#输出键为2的值
print(tinydict)
print(tinydict.keys())
print(tinydict.values())
#字典的关键字必须为不可变类型且不重复