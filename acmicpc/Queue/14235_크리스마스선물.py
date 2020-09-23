import heapq

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

hq = []

for i in range(N):
    if not A[i][0]:  # 0 일때
        if not len(hq):
            print(-1)
        else:
            print(heapq.heappop(hq)[1])
    else:
        temp = A[i][1:]  # A[i]의 0번째 요소를 제거함, 즉 선물 갯수만 빼고 선물만 큐에 넣게함
        for i in range(A[i][0]):
            heapq.heappush(hq, [-temp[i], temp[i]])
