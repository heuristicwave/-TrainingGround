import sys
input = sys.stdin.readline

# 0:N/1:E/2:S/3:W
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def clean(x, y, d):
    global cnt

    if board[x][y] == 0:
        board[x][y] = 2  # clean up
        cnt += 1

    for _ in range(4):
        # 왼쪽으로 방향 전환 하는 효과 0은 3, 나머지는 -1
        nd = (d+3) % 4
        nx, ny = x + dx[nd], y + dy[nd]

        if board[nx][ny] == 0:
            clean(nx, ny, nd)
            return

        d = nd  # 방향 복구

    nd = (d+2) % 4  # 후진을 위한 방향 재설정
    nx, ny = x + dx[nd], y + dy[nd]

    if board[nx][ny] == 1:
        return
    clean(nx, ny, d)


n, m = map(int, input().split())
r, c, direction = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
clean(r, c, direction)
print(cnt)
