'''
문제 조건 파악
1칸+1칸+1칸 => 연속된 3 계단이라 불가
2칸 + 1칸, 2칸 => 경우의 수 2가지
위 조건 맞추려 3부터 시작함(3이후 부터 점화식)
즉, dp 0부터 2까지는 직접 정해줘야함
'''
# Solution 1
# DP를 주어진 N만큼 할당하면, 실수로 인한 런타임 오류 날 확률 올라감

N = int(input())
A = [int(input()) for _ in range(N)]
dp = [0] * (N)

if N == 1:
    print(A[0])
elif N == 2:       # if로 하면 dp를 N만큼 선언했기 때문에 여기서 런타임
    print(A[0]+A[1])
else:
    dp[0] = A[0]
    dp[1] = A[0]+A[1]
    dp[2] = max(A[1]+A[2], A[0]+A[2])

    for i in range(3, N):
        dp[i] = max(dp[i-2] + A[i], dp[i-3] + A[i-1] + A[i])

    print(dp[-1])

# Solution 2
# 차라리 DP를 문제에서 주어진 최대값으로 할당하면 0을 참조하니 런타임에러 피할 수 있음

N = int(input())
# 여기도 12라인 처럼 한번에 받으면, 런타임 위험 증가 EX) N = 1 이면, A[2]에서 런타임
A = [int(input()) for _ in range(301)]
dp = [0] * (301)

for i in range(N):
    A[i] = int(input())

dp[0] = A[0]
dp[1] = A[0] + A[1]
dp[2] = max(A[1] + A[2], A[0] + A[2])

for i in range(3, N):
    dp[i] = max(dp[i-3] + A[i-1] + A[i], dp[i-2] + A[i])

print(dp[N-1])

'''
즉, N개수 만큼 A혹은 DP를 할당하나 문제의 최대 조건으로 할당하나
공간, 시간 복잡도 차이는 미미하니 문제 조건의 최댓값으로 할당하는 것을 지향
N개수 만큼 할당하면 반례를 고려하는 만큼 코드가 더 길어짐
'''
