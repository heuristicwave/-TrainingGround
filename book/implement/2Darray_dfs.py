import sys
import time

sys.stdin = open("input.txt", "r")
start = time.time()


def check(x, y):
    global cnt
    my_map[x][y] = 2
    cnt += 1

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx > row-1 or ny < 0 or ny > col-1:
            continue
        if my_map[nx][ny] == 0:
            check(nx, ny)


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

row, col = map(int, input().split())
x, y, direction = map(int, input().split())
cnt = 0
my_map = []

for i in range(col):
    my_map.append(list(map(int, input().split())))  # list 통째로 넣기
    # my_map[i][0], my_map[i][1], my_map[i][2], my_map[i][3] = map(int, input().split())

if my_map[x][y] != 0:
    print(0)

check(x, y)

print(cnt)
print("time :", time.time() - start)
