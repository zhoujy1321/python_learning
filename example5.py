#python推导式
#从一个数据序列构建另一个新的数据序列的结构体

#列表推导式：[表达式 for 变量 in 列表 if 条件]
names = ['bob','tom','alice','jerry','wendy','smith']
new_names = [name.upper() for name in names if len(name)>3]
print(new_names)
multiples = [i for i in range(30) if i%3==0]
print(multiples)

#字典推导式：{ key_expr: value_expr for value in collection }
listdemo = ['google','runoob','taobao']
new_dicts = {key:len(key) for key in listdemo}
print(new_dicts)
numdic = {x:x**2 for x in range(3,10)}
print(numdic)

#集合推导式：{ expression for item in Sequence if conditional }
a = {y for y in 'asdfghjkl' if y not in 'abcdefg'}
print(a)

#元组推导式：(expression for item in Sequence if conditional )
#与前面不同的是，元组推导式返回的是一个生成器对象，返回值需要使用tuple()函数
b = (z for z in range(1,10))
print(b)
print(tuple(b))