A, B, C = map(int, input().split())

def solve(num, div):
    if div == 1:
        return num % C
    out = solve(num, div//2)
    return out**2 % C if div%2==0 else out**2 * A % C

print(solve(A, B))

# """ Shortest way """
# print(pow(*map(int, input().split())))