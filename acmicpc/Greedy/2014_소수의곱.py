import heapq
import copy

K, N = map(int, input().split())
A = list(map(int, input().split()))

lst, ck = copy.deepcopy(A), set()

heapq.heapify(lst)  # heap으로 바꿈
ith = 0

while ith < N:
    mn = heapq.heappop(lst)
    if mn in ck:
        continue
    ith += 1
    ck.add(mn)
    for i in A:
        if mn * i < 2 ** 32:
            heapq.heappush(lst, mn*i)

print(mn)
