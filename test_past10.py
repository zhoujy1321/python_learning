def GetPrimeNum(a,b):
    for num in range(a,b+1):
        if num > 1:
            for i in range(2,int(num**0.5 + 1)):
                if (num % i) == 0:
                    break
            else:
                print(num)

lower = int(input('input the lower num:'))
upper = int(input('input the upper num:'))
GetPrimeNum(lower,upper)