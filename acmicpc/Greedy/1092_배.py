import sys
import time
from collections import deque

sys.stdin = open("input.txt", "r")
start = time.time()

N = int(input())    # # of craines
c_list = sorted(map(int, sys.stdin.readline().split()), reverse=True)
M = int(input())    # # of boxes
b_list = sorted(map(int, sys.stdin.readline().split()), reverse=True)

positions = [0] * N
finished = [False] * M    # 배열요소 삭제하면 반복문 길이 달라져서 다른것과 비교함

if c_list[0] < b_list[0]:
    print(-1)
    sys.exit()

move, count = 0, 0
numOfBoxes = len(b_list)

while True:
    if count == numOfBoxes:
        break

    for i in range(N):
        # 0부터 자리를 점검하며 체크하면서 box와 비교
        while positions[i] < len(b_list):
            if not finished[positions[i]] and c_list[i] >= b_list[positions[i]]:
                finished[positions[i]] = True
                positions[i] += 1
                count += 1
                break
            positions[i] += 1
    move += 1


print(move)
print("time :", time.time() - start)
