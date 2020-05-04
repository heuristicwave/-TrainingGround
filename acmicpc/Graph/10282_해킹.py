# 우선순위 큐 O(NlogD)

import heapq as hq
import sys
input = sys.stdin.readline  # sys.stdin.readline() > raw_input() > input()


def dijkstra(start):
    heap_data = []
    hq.heappush(heap_data, (0, start))   # 0부터 특정 정점까지(start)
    distance[start] = 0
    while heap_data:
        dist, now = hq.heappop(heap_data)
        if distance[now] < dist:
            continue
        for i in adj[now]:  # 정점과 연결된 다른 점 확인, i == (x, cost)
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost   # update
                hq.heappush(heap_data, (cost, i[0]))  # put update data


for _ in range(int(input())):
    n, m, start = map(int, input().split())
    adj = [[] for i in range(n + 1)]
    distance = [1e9] * (n + 1)  # initialize to infinite
    for _ in range(d):
        x, y, cost = map(int, input().split())
        adj[y].append((x, cost))
    dijkstra(start)

    count = 0
    max_distance = 0
    for i in distance:
        if i != 1e9:
            count += 1
            if i > max_distance:
                max_distance = i
    print(count, max_distance)
