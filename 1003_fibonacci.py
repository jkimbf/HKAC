import sys

input = sys.stdin.readline
fib = {x: -1 for x in range(0, 41)}

def fibonacci(n):
    if 0 <= n <= 1:
        return n
    
    if fib[n] != -1:
        return fib[n]
    fib[n] = fibonacci(n-1) + fibonacci(n-2)
    return fib[n]

for _ in range(int(input())):
    n = int(input())
    if n == 0:
        print("1 0")
    elif n == 1:
        print("0 1")
    else:
        n_1 = fibonacci(n-1)
        print(*[n_1, n_1+fibonacci(n-2)], sep=" ")