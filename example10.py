#python列表
import operator


list = ['Google', 'Runoob', "Zhihu", "Taobao", "Wiki"]
print ("list[1]: ", list[1])# 读取第二位
print ("list[1:-2]: ", list[1:-2])# 从第二位开始（包含）截取到倒数第二位（不包含）




print('----------------------------\n')
#可以对列表的数据进行更新，或者用append()方法添加列表项
list = ['Google', 'Runoob', 1997, 2000]
print ("第三个元素为 : ", list[2])
list[2] = 2001
print ("更新后的第三个元素为 : ", list[2])
list1 = ['Google', 'Runoob', 'Taobao']
list1.append('Baidu')
print ("更新后的列表 : ", list1)



print('----------------------------\n')
#可以用del语句删除列表中的元素
list = ['Google', 'Runoob', 1997, 2000]
print ("原始列表 : ", list)
del list[1]
print ("删除第二个元素 : ", list)



print('----------------------------\n')
#列表截取和拼接
L = ['mci','ars','tot','che']
print(L[2],L[-1])
print(L[1:])
print('更新前列表:',L)
L += ['liv','mun']
print('更新后列表:',L)



print('----------------------------\n')
#嵌套列表
a = ['a','b','c']
b = ['d','e','f']
x = [a,b]
print(x[0],x[1])
print(x[0][1],x[1][2])



print('----------------------------\n')
#列表比较，相同true，不同false
c = ['a','b','c']
print('operator.eq(a,b)',operator.eq(a,b))
print('operator.eq(a,c)',operator.eq(a,c))



#python列表函数
'''
len(list)
max(list)   min(list)
list(seq)                            #将元组()转化为列表[]
list.append(obj)
list.count(obj)                      #统计某个元素在列表中出现的次数
list.extend(obj)                     #在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
list.index(obj)                      #从列表中找出某个值第一个匹配项的索引位置
list.insert(index,obj)               #从列表中找出某个值第一个匹配项的索引位置
list.pop([index=-1])                 #移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
list.remove(obj)                     #移除列表中某个值的第一个匹配项
list.reverse()
list.sort( key=None, reverse=False)  #对原列表进行排序
list.clear()    
'''