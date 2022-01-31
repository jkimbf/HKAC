from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    n = int(input())
    nums = []
    nums.append([0 for _ in range(n)])
    for _ in range(2):
        nums.append(
            list(map(int, input().split()))
        )

    for i in range(1, n):
        for j in range(3):
            nums[j][i] += max(nums[j-1][i-1], nums[j-2][i-1])
    
    print(max([nums[i][n-1] for i in range(3)]))