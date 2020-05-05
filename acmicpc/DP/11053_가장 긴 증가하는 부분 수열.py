# 앞에서부터 하나씩 dp로
# D[j] = array[i]를 마지막 원소로 가지는 부분 수열의 최대 길이
# D[i] = max(D[i], D[j]+1) if array[j] < array[i]

n = int(input())
a = list(map(int, input().split()))

dp = [1] * (n)

# key point : line 10 ~ 11. iterate
for i in range(1, n):
    for j in range(0, i):
        if a[j] < a[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
