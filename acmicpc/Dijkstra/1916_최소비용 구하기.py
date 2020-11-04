import sys
from heapq import heappop, heappush

N, M = int(input()), int(input())

graph = [[] for i in range(N+1)]
dist = [sys.maxsize] * (1001)

for _ in range(M):
    s, d, c = map(int, input().split())  # start, destination, cost
    graph[s].append((d, c))


def dijkstra(start):
    q = []
    heappush(q, (start, 0))  # start부터 거리 0으로 시작
    dist[start] = 0

    while q:
        now, distance = heappop(q)
        for i in graph[now]:    # node에 담긴 다음 장소 순회
            cost = distance + i[1]
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heappush(q, (i[0], cost))
        '''
        # 튜플을 다루는 더 직관적인 코드
        for node, weight in graph[now]:
        '''


start, finish = map(int, input().split())
dijkstra(start)
print(dist[finish])
