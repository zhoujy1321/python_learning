#fibonacci series
a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a+b

#end关键字，可用于将结果输出到同一行，或者在输出的末尾添加不同的字符
a, b = 0, 1
while b < 10:
    print(b,end=',')
    a, b = b, a+b  