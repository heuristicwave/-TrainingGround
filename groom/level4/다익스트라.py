import sys
import heapq as hq
input = sys.stdin.readline

n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]
distance = [sys.maxsize] * (n+1)

for _ in range(m):
    s, d, v = map(int, input().split())
    adj[s].append((d, v))
    adj[d].append((s, v))


def dijkstra(start):
    heap_data = []
    hq.heappush(heap_data, (0, start))
    distance[start] = 0

    while heap_data:
        dist, now = hq.heappop(heap_data)
        if distance[now] < dist:
            continue
        for x, value in adj[now]:  # 정점과 연결된 다른 점 확인
            cost = dist + value
            if distance[x] > cost:
                distance[x] = cost
                hq.heappush(heap_data, (cost, x))


dijkstra(int(input()))

for i in range(1, n+1):
    print(f'{i}: {distance[i]}')
