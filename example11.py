#python元组
'''
元组语法与列表类似，不同点在于：
元组不能修改和删除单个值，只能整个元组拼接或者删除整个元组
'''

#元组运算符
'''
len((1,2,3))
(1,2,3)+(4,5,6)
('hi!')*4
2 in (1,2,3)
for x in (1,2,3)
    print(x,end='')
'''

#元组也能截取和索引

#元组内置函数
'''
len(tuple)
max(tuple)
min(tuple)
tuple(iterable)  将列表转化为元组
'''

#元组是不可变的：元组所指向的内存中的内容不可变，对一个元组重新赋值会改变为新的地址。