# Longest Common Subsequence : O(N**2)
# DP를 어떻게 만들까 1차원 OR 2차원 => 주어진 문자열 2개, 2차원 배열
# 2차원 배열 경우의 수를 먼저 그림으로 그리고 점화식으로 옮기기
# 문자열 길이를 늘려가며 가장 긴 수열 찾기

#   0 C A P C A K
# 0 0 0 0 0 0 0 0
# A 0 0 1 1 1 1 1
# C 0 1 1 1 2 2 2
# A 0 1 2 2 2 3 3
# Y 0 1 2 2 2 3 4
# K 0 1 2 2 2 3 4
# P 0 1 2 3 3 3 4

x, y = input(), input()

# initialize to 0 include empty set => len + 1
dp = [[0] * (len(y) + 1) for _ in range(len(x) + 1)]

for i in range(1, len(x) + 1):
    for j in range(1, len(y) + 1):
        if x[i-1] == y[j-1]:    # If characters are the same
            dp[i][j] = dp[i-1][j-1] + 1  # diagonal direction + 1
        else:   # Bigger of the left and top
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print(dp[len(x)][len(y)])   # 가장 마지막
