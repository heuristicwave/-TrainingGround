'''
문제 조건 파악
1칸+1칸+1칸 => 연속된 3 계단이라 불가
2칸 + 1칸, 2칸 => 경우의 수 2가지
위 조건 맞추려 3부터 시작함(3이후 부터 점화식)
즉, dp 0부터 2까지는 직접 정해줘야함
'''
step_len = int(input())
dp = [0] * (step_len)
a = [int(input()) for _ in range(step_len)]

dp[0] = a[0]
dp[1] = max(a[0]+a[1], a[1])
dp[2] = max(a[0]+a[2], a[1]+a[2])

for i in range(3, step_len):
    dp[i] = max(dp[i-2]+a[i], dp[i-3] + a[i-1] + a[i])
    # print(dp) # debug

print(dp[-1])
