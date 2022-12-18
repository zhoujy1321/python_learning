a = float (input('input the value of a:'))
b = float (input('input the value of b:'))
c = float (input('input the value of c:'))
s = (a + b + c)/2
area = (s*(s - a)*(s - b)*(s - c)) ** 0.5
print(a,b,c,'consist a area of',area)