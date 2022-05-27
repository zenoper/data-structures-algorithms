#  0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181

def Fibo(n):
    if n < 2:
        return n
    return Fibo(n-1) + Fibo(n-2)

print(Fibo(30))

def memoizedFibo(n):
    cache = {}
    def fib(n):
        if n in cache:
            return cache[n]
        else:
            if n < 2:
                return n
            else:
                cache[n] =  fib(n-1) + fib(n-2)
                return cache[n]
    return fib(n)

print(memoizedFibo(30))