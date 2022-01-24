from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)

input = stdin.readline
N = int(input())
checker = {n: [] for n in range(N)}#[[False]*N for _ in range(N)]
output = [-1]*N

for _ in range(N-1):
    a, b = map(int, input().split())
    checker[a-1].append(b-1)
    checker[b-1].append(a-1)

def search(i):
    for c in checker[i]:
        if output[c] == -1:
            output[c] = i+1
            search(c)

search(0)
print(*output[1:], sep='\n')