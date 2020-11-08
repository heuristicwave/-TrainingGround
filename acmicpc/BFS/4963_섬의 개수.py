from collections import deque

dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    board = [list(map(int, input().split())) for _ in range(h)]

    def bfs(x, y):
        board[x][y] = 0  # visited : 1 => 0
        q = deque()
        q.append((x, y))

        while q:
            x, y = q.popleft()
            for i in range(8):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < h and 0 <= ny < w and board[nx][ny] == 1:
                    q.append((nx, ny))
                    board[nx][ny] = 0

    cnt = 0
    for i in range(h):
        for j in range(w):
            if board[i][j] == 0:
                continue
            bfs(i, j)
            cnt += 1
    print(cnt)
