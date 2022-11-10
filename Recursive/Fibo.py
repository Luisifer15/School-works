def iFibo(N):
    Val1 = 0
    Val2 = 1
    Total = Val1 + Val2
    if N <= 0:
        print('Value cannot be 0 or lower')
    elif N == 1:
        print(Val1)
    else:
        print(Val1)
        print(Val2)
        for I in range(2,N):
            print(Total)
            Val1 = Val2
            Val2 = Total
            Total = Val1 + Val2

def Fibonacci(N): 
    if N == 0:
        return N
    elif N == 1:
        return N
    else:
        return Fibonacci(N - 1) + Fibonacci(N - 2)

def rFibo(n):
    if n <= 0:
        print('Value cannot be 0 or lower')
    for i in range(n):
       print(Fibonacci(i))


iFibo(10)
rFibo(10)

