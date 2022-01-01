def fac(x):
    for i in range(1, x):
        x *= i
    return x

N, M = map(int, input().split())
print(fac(N)//(fac(M)*fac(N-M)))