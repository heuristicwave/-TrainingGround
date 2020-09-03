import sys
import time
from collections import deque

sys.stdin = open("input.txt", "r")
start = time.time()

N, M = map(int, input().split())
battleground = [list(input()) for _ in range(N)]   # put 2D array
visited = [[False] * M for _ in range(N)]

q = deque()
w_team, b_team = 0, 0


def getMilitaryPower(i, j):
    q.append((i, j))
    visited[i][j] = True
    cnt = 1

    while q:
        x, y = q.popleft()
        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if visited[nx][ny] is False and battleground[nx][ny] == battleground[x][y]:
                q.append((nx, ny))
                visited[nx][ny] = True
                cnt += 1
    return cnt


for i in range(M):
    for j in range(N):
        if visited[i][j] == False:
            ret = getMilitaryPower(i, j)
            if battleground[i][j] == 'W':
                w_team += ret ** 2
            else:
                b_team += ret ** 2

print(w_team, b_team)
print("time :", time.time() - start)
