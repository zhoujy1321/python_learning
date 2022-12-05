#python字典
'''
字典是一种可变容器模型，可存储任意种类对象
格式 : d = {key1 : value1, key2 : value2, key3 : value3}
'''
#键必须唯一，值不必；键只能取不可变类型如字符串和数字，值可以取任何数据类型
tinydict = {'no1':'MCI', 'no2':'ARS', 'no3':'LIV', 3:2}
print(tinydict)

#创建空字典
emptydict = {}
print(emptydict)
print("Length:", len(emptydict))
print(type(emptydict))

#访问字典


#修改字典
tinydict['no3'] = 'MUN'
print('tinydict[no3]:', tinydict['no3'])

#删除字典元素
del tinydict['no2']
print(tinydict)
tinydict.clear()
print(tinydict)
del tinydict

#键必须不可变，如数字、字符串、元组，而不能用列表
#不能同一个键，相同取后者

#字典内置函数
'''
len(dict)
str(dict)   输出字典,打印字典的字符串表示
type(dict)  返回输入的变量类型，如果是字典返回字典类型
'''

#字典内置方法
'''
dlct.clear()
dict.copy()
dict.fromkeys() 创建一个新字典
dict.get(key)
key in dict
dict.items()
dict.keys()
dict.update(dict2)
'''