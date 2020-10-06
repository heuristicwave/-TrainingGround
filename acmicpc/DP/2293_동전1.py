N, K = map(int, input().split())
A = [int(input()) for _ in range(N)]

dp = [0] * 10001
dp[0] = 1

for i in A:
    for j in range(i, K+1):
        dp[j] += dp[j-i]

print(dp[K])
