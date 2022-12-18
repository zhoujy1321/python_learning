def detect(num):
    flag = num
    sum = 0
    length = len(str(num))
    while num > 0:
        temp = num % 10
        sum += temp ** length
        num = num // 10
        if flag == sum:
            print(flag,'is an amstrout number')
    return True

num = int(input('plz input the range u need to detect:'))
for i in range(1,num):
    detect(i)