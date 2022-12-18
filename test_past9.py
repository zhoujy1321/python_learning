def iszhishu(a):
    if a == 1:
        print('special one.')
    else:
        for i in range (2,(int(num ** 0.5) + 1)):
            if (num % i) == 0:
                return False
        return True

num = int(input('input the number:'))
print(iszhishu(num))