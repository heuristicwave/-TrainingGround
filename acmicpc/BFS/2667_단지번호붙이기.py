import sys
import time
from collections import deque

sys.stdin = open("input.txt", "r")
start = time.time()

N = int(input())
town = [list(map(int, input())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

q = deque()


def bfs(i, j, cnt):
    q.append((i, j))
    visited[i][j] = cnt
    house = 1   # 1 주변에 모두 0 만 있는 경우를 대비해 1부터 시작

    while q:
        x, y = q.popleft()
        for dx, dy in (0, 1), (1, 0), (-1, 0), (0, -1):
            nx, ny = dx + x, dy + y
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == 0 and town[nx][ny] == 1:
                    q.append((nx, ny))
                    visited[nx][ny] = cnt   # 해당 단지로 바꿔줌
                    house += 1

    return house


cnt = 0
num_house = []  # 단지별 개수를 저장
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0 and town[i][j] == 1:
            cnt += 1
            num_house.append(bfs(i, j, cnt))

num_house.sort()    # 문제 조건 오름차순으로 출력하라!

print(cnt)
# for i in num_house:   # 0.0059
#     print(i, end='\n')
print("\n".join(map(str, num_house)))   # 0.0030

'''
list 출력하는 방법

- 요소가 int 형일때 (str로 바꿔서 출력)
print("\n".join(map(str, num_house)))  

- 요소가 str 형일때
print('\n'.join(num_house)) 
'''

print("time :", time.time() - start)
