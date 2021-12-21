def gcd(x, y):
    return x if y == 0 else gcd(y, x%y)
a, b = map(int, input().split())
out = gcd(a, b)
print(out)
print(abs(a*b)//out)