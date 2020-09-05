import sys
import time
from collections import deque

"""
주의 사항
- 가로 세로 n, m 배열 크기 넘으면 error
- list 입력 받기
- 방문값 2번... check ...
"""
sys.stdin = open("input.txt", "r")
start = time.time()

N, M = map(int, input().split())
field = [list(input()) for _ in range(M)]
checked = [[False] * N for _ in range(M)]

w_power, b_power = 0, 0
q = deque()


def bfs(x, y):
    checked[x][y] = True    # 여기 없으면 ret 값 9 1 8 7인데 10 1 9 8나옴
    q.append((x, y))
    cnt = 1

    while q:
        x, y = q.popleft()
        for dx, dy in (1, 0), (0, -1), (-1, 0), (0, 1):
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue

            # W일 때 B일 때 코드 중복을 줄이기 위해 이전 필드값과 비교
            if checked[nx][ny] == False and field[nx][ny] == field[x][y]:
                cnt += 1
                q.append((nx, ny))
                checked[nx][ny] = True

    return cnt


for i in range(M):
    for j in range(N):
        if checked[i][j] == False:  # memoization for reduce bfs call
            ret = bfs(i, j)
            if field[i][j] == 'W':
                w_power += ret ** 2
            else:
                b_power += ret ** 2

print(w_power, b_power)

print("time :", time.time() - start)
