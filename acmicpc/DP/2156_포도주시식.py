'''
!! CREATE TABLE, LIKE FIBO !!

WINES   1  2   3    4      5    6
CASES   1 1&2 1&2  2&3  1&2&4&5
              1&3 1&3&4  1&3&4
              2&3 1&2&4  2&3&5
              
!! AFTER THAT, MAKE THE RECURRENCE RELATION !!
'''
N = int(input())
wines = [0]  # 0은 0부터 두고, 편의성을 위해 1부터 채워나감

for _ in range(N):
    wines.append(int(input()))

dp = [0] * (N+1)
dp[1] = wines[1]

if N > 1:
    dp[2] = dp[1]+wines[2]

for i in range(3, N+1):
    dp[i] = max(dp[i-1], dp[i-3]+wines[i-1]+wines[i], dp[i-2]+wines[i])

print(dp[N])
