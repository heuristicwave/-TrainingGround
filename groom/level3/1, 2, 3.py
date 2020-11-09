'''
n이 1일 때 1가지, 2일 때 2가지, 3일 때 3가지
4는 (dp[3] 경우 + 1만 붙힘) + (dp[2] 경우 + 1만 붙힘)
즉, dp[1], dp[2], dp[3]의 합니다.
4부터 dp[i-1] + dp[i-2] + dp[i-3] 점화식 생성
'''

n = int(input())
dp = [1, 2, 4]

if n > 3:
    for i in range(3, n):
        dp_i = dp[i-1] + dp[i-2] + dp[i-3]
        dp.append(dp_i)
print(dp[n-1])
