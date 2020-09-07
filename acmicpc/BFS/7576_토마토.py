import sys
import time
from collections import deque

sys.stdin = open("input.txt", "r")
start = time.time()

M, N = map(int, input().split())
warehouse = [list(map(int, input().split())) for _ in range(N)]
q = deque()

# getTomatoStatus
for i in range(N):
    for j in range(M):
        if warehouse[i][j] == 1:
            q.append((i, j))

day = -1

while q:
    day += 1
    for _ in range(len(q)):  # 큐의 길이만큼 돌리는게 포인트...
        x, y = q.popleft()
        for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if warehouse[nx][ny] == -1 or warehouse[nx][ny] == 1:
                    continue
                warehouse[nx][ny] = 1
                q.append((nx, ny))

for row in warehouse:
    if 0 in row:
        day = -1
        break

print(day)

print("time :", time.time() - start)
