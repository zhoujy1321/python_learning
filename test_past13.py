def fibonacci(num):
    n0 = 0
    n1 = 1
    print(n1)
    for i in range(1,num):
        n = n0 + n1
        n0 = n1
        n1 = n
        print(n)
    return True

num = int(input('input how many numbers u need:'))
fibonacci(num)