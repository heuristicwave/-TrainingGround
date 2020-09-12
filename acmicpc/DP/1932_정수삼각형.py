import sys

sys.stdin = open("input.txt", "r")

N = int(input())
# dp[i][j] : i, j에 도착했을 때 최대 값
triangle = [[0 for _ in range(N+1)] for i in range(N+1)]
dp = [[0 for _ in range(N+1)] for i in range(N+1)]

for i in range(1, N+1):
    tmp = list(map(int, input().split()))
    for j in range(1, i+1):
        triangle[i][j] = tmp[j-1]

for i in range(1, N+1):
    for j in range(1, i+1):
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]

print(max(dp[-1]))
