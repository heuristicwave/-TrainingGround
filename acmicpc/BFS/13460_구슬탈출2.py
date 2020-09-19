'''
4시간 동안 풀었는데 어디가 틀렸는지 모르겠다 ㅠㅠ

참고 풀이 : https://jeongchul.tistory.com/666
'''

import sys
import time
from collections import deque

sys.stdin = open("input.txt", "r")
start = time.time()

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

rx, ry = 0, 0   # red
bx, by = 0, 0   # blue
answer = 1

for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            rx, ry = i, j
        elif board[i][j] == 'B':
            bx, by = i, j

visited = [[[[False] * M for _ in range(N)]
            for _ in range(M)] for _ in range(N)]
visited[rx][ry][bx][by] = True


def bfs():
    global answer
    q.append((rx, ry, bx, by, answer))

    while q:
        crx, cry, cbx, cby, answer = q.popleft()
        if answer > 10:
            break

        for ix, iy in (0, 1), (1, 0), (0, -1), (-1, 0):
            print('direction', ix, iy)
            nrx, nry = crx + ix, cry + iy
            nbx, nby = cbx + ix, cby + iy

            # 벽이거나 구멍이면 안됨
            while board[nrx][nry] != '#' and board[nrx][nry] != 'O':
                nrx += ix
                nry += iy
            if board[nrx][nry] == '#':
                nrx -= ix
                nry -= iy
            while board[nbx][nby] != '#' and board[nbx][nby] != 'O':
                nbx += ix
                nby += iy
            if board[nbx][nby] == '#':
                nbx -= ix
                nby -= iy

            if board[nrx][nry] == 'O':
                if board[nbx][nby] != 'O':
                    print(answer)
                    return
                elif board[nbx][nby] == 'O':
                    continue

            print('1', nrx, nry, nbx, nby)
            print('answer : ', answer)
            # ! POINT ! 한 칸에 2개가 동시에 있으면 조정(굴러온 거리 비교)
            if nrx == nbx and nry == nby:
                if board[nrx][nry] != 'O':
                    rd = abs(nrx - crx) + abs(nry - cry)
                    bd = abs(nbx - cbx) + abs(nby - cby)
                    print('cc', crx, cry, cbx, cby)
                    print('rdbd', rd, bd)
                    if rd > bd:
                        nrx -= ix
                        nry -= iy
                    else:
                        nbx -= ix
                        nby -= iy

            print('2', nrx, nry, nbx, nby)

            if not visited[nrx][nry][nbx][nby]:
                visited[nrx][nry][nbx][nby] = True
                # answer += 1, 전역 그대로 쓰면 중복 처리 못함
                q.append((nrx, nry, nbx, nby, answer + 1))

    print(-1)


q = deque()
bfs()

print(answer if answer < 10 else -1)
print("time :", time.time() - start)
