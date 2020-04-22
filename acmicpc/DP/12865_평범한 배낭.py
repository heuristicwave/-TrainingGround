# O(NK), 냅색알고리즘
# 모든 무게에 대하여 최대 가치 저장!

n, k = map(int, input().split())
dp = [[0] * (k+1) for _ in range(n+1)]

for i in range(1, n+1):
    w, v = map(int, input().split())
    for j in range(1, k+1):  # dp 1부터 k까지 차례로 갱신, i(행)만큼
        if j < w:
            dp[i][j] = dp[i-1][j]   # 위에서 그대로 값 내림
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)

print(dp[n][k])

# 개선 => 1차원 배열로 접근
# 최댓값 찾기 뒤에서부터 접근
# dy = [0] * (k+1)
# for _ in range(n):
#     w, v = map(int, input().split())
#     for i in range(k, w-1, -1):
#         dy[i] = max(dy[i], dy[i-w]+v)

# print(dy[k])
