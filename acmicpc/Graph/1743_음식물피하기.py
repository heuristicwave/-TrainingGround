from collections import deque

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(K)]

board = [[False] * M for _ in range(N)]
check = [[False] * M for _ in range(N)]
answer = 0

for r, c in A:
    board[r-1][c-1] = True


def bfs(x, y):

    q.append((x, y))
    check[x][y] = True
    cnt = 1

    while q:
        x, y = q.popleft()
        # print(x, y, cnt)
        for i, j in (0, 1), (1, 0), (0, -1), (-1, 0):
            nx, ny = x + i, y + j
            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] and not check[nx][ny]:
                    check[nx][ny] = True
                    q.append((nx, ny))
                    cnt += 1

    return cnt


q = deque()
for i in range(N):
    for j in range(M):
        if board[i][j] and not check[i][j]:
            # print('start', board[i][j], i, j)
            ret = bfs(i, j)
            if ret > answer:
                answer = ret

print(answer)
