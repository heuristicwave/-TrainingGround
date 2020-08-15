import sys
import time

sys.stdin = open("input.txt", "r")
start = time.time()

dx = [-1, 1, 2, 2, 1, -1, -2, -2]
dy = [-2, -1, -1, 1, 2, 2, 1, -1]

N, cnt = input(), 0
# ord('a') >> 97
x, y = ord(N[0]) - 96, int(N[1])

for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > 8 or ny > 8:
        continue
    cnt += 1

print(cnt)
print("time :", time.time() - start)
