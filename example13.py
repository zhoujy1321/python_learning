#python集合
'''
集合是一个无序的不重复元素序列
用大括号{}或者set()函数创建集合,创建空集合必须用set()而不是{},{}是用来创建空字典
'''

basket = {'apple', 'orange', 'pear', 'banana', 'strawbarry', 'apple'}
print(bool('orange' in basket))

a = set('qwertyuiop')
b = set('qwerty')
print(a)
print(a - b)
print(a | b)
print(a & b)
print(a ^ b)

#集合推导式
an = {x for x in a if x not in b}
print(an)


print('_____________________________')
#集合的基本操作
basket.add('watermalon')
print(basket)
basket.update({1,2})
print(basket)#添加元素

#basket.remove('1')
#rint(basket)#如果移除的元素不存在会报错
basket.discard('watermalon')
print(basket)#不会报错
x = basket.pop()#随机删除一个
print(x)

#计算集合元素个数
len(x)

#清空集合
x.claer()

