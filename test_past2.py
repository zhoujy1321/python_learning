import cmath
a = float (input('input the value of a:'))
b = float (input('input the value of b:'))
c = float (input('input the value of c:'))
delta = b**2 - 4*a*c
res1 = (-b + cmath.sqrt(delta))/(2*a)
res2 = (-b - cmath.sqrt(delta))/(2*a)
print('the results are:{0} and {1}'.format(res1,res2))