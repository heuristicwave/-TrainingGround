# https://blueshw.github.io/2016/01/20/shallow-copy-deep-copy/
import copy

N, A = int(input()), list(map(int, input().split()))
DP = copy.deepcopy(A)   # DP[i] : i까지 왔을 때, 합의 최대

for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            DP[i] = max(A[i] + DP[j], DP[i])

print(max(DP))

# return 값의 요소 구하기, 직접 해보기

# N, A = int(input()), list(map(int, input().split()))
# DP = copy.deepcopy(A)   # DP[i] : i까지 왔을 때, 합의 최대
# rev = [i for i in range(N)]

# idx = 0

# for i in range(1, N):
#     for j in range(i):
#         if A[i] > A[j] and DP[i] < A[i] + DP[j]:
#             DP[i] = A[i] + DP[j]
#             rev[i] = j

#     if DP[idx] < DP[i]:
#         idx = i

# print(DP[idx])
# while rev[idx] != idx:
#     print(A[idx], seq=" ")
#     idx = rev[idx]

# print(A[idx])
