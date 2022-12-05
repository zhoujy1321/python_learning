#python迭代器和生成器
'''
迭代器是一个可以记住遍历位置的对象
迭代器对象从集合的第一个元素开始访问,直到所有的元素被访问完结束
迭代器两个基本方法:iter(),next()
字符串,列表和元组对象都可以用于创建迭代器
'''
import sys
'''
list1 = [1,2,3,4]
it1 = iter(list1)     #创建迭代器对象
print(next(it1))     #输出迭代器的下一个元素
print(next(it1))
for x in it1:
    print(x,end=' ')#迭代器对象可以使用常规for语句进行遍历

list2 = [4,5,6,7]
it2 = iter(list2)
while True:
    try:
        print(next(it2))
    except StopIteration:
        sys.exit()
'''


#创建一个迭代器
'''
#把一个类作为一个迭代器需要在类中实现两个方法_iter()_和_next()_

class Mynumbers:
    def _iter_(self):
        self.a = 1
        return self

    def _next_(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = Mynumbers()
myiter = iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
'''


#Stoplteration用于标识迭代完成，表示无限循环
'''
#生成器
def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if(counter > n):
            return
        yield a
        a, b = b, a+b
        counter += 1
f = fibonacci(10)

while True:
    try:
        print(next(f), end=' ')
    except StopIteration:
        sys.exit()
'''