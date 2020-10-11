'''
Dijkstra - graph / visited / distance
'''

from heapq import heappop, heappush
import sys

input = sys.stdin.readline
INF = int(1e9)

V, E = map(int, input().split())
start = int(input())

graph = [[] for i in range(V+1)]
visited = [False] * (V+1)
distance = [INF] * (V+1)

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

'''
!! TIME OUT !!

def get_shortest_node():
    min_value = INF
    index = 0
    for i in range(1, V+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index


def dijkstra(start):
    distance[start] = 0 # 시작 노드 초기화
    visited[start] = True

    for i in graph[start]:  distance[i[0]] = i[1]
    for i in range(V-1):    # 시작 노드를 제외한 V-1개에 대해 반복
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문처리
        now = get_shortest_node()
        visited[now] = True

        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:   distance[j[0]] = cost
'''


def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 거리 0 설정
    heappush(q, (0, start))
    distance[start] = 0
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heappop(q)
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접 노드 확인
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heappush(q, (cost, i[0]))


dijkstra(start)

for i in range(1, V+1):
    print(distance[i] if distance[i] != INF else 'INF')
