import heapq

N = int(input())
A = [int(input()) for _ in range(N)]

hq = []

for i in range(N):
    if not A[i]:  # 0 일때
        if not len(hq):
            print(0)
        else:
            print(heapq.heappop(hq))
    else:
        heapq.heappush(hq, A[i])
