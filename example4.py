#python3数据类型转换
#隐式类型转换：自动完成
num_int = 123
num_flo = 1.23
num_new = num_flo + num_int
print('datatype of num_int:',type(num_int))
print('datatype of num_flo:',type(num_flo))
print('datatype of num_new:',type(num_new),';value of num_new',num_new)
print('--------------------------\n')
#显式类型转换：使用类型函数转换
x = int(2.8)
y = float(2)
z = str(2.0)
print('datatype of x:',type(x),'datatype of y',type(y),'datatype of z',type(z))