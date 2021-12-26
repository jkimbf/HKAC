N = int(input())
dp = list(range(-1, N))

for i in range(1, N+1):
    if i % 3 == 0 and i % 2 == 0:
        dp[i]= min(dp[i//3]+1, dp[i//2]+1, dp[i-1]+1, dp[i])
    if i % 3 == 0 and not i % 2 == 0:
        dp[i]= min(dp[i//3]+1, dp[i-1]+1, dp[i])
    if not i % 3 == 0 and i % 2 == 0:
        dp[i] = min(dp[i//2]+1, dp[i-1]+1, dp[i])
    else:
        dp[i] = min(dp[i-1]+1, dp[i])

print(dp[N])