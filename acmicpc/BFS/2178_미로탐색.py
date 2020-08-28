import sys
from collections import deque

sys.stdin = open("input.txt", "r")

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

n, m = map(int, input().split())
graph = [list(map(int, list(input()))) for _ in range(n)]   # put 2D array


visited = [[False] * m for _ in range(n)]
dist = [[0]*m for _ in range(n)]

visited[0][0] = True
dist[0][0] = 1

q = deque()
q.append((0, 0))    # graph & visited 도 0, 0 부터 시작함

while q:
    x, y = q.popleft()
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            if visited[nx][ny] is False and graph[nx][ny] == 1:
                q.append((nx, ny))
                dist[nx][ny] = dist[x][y] + 1
                visited[nx][ny] = True

print(dist[n - 1][m - 1])
