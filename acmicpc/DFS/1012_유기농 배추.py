import sys
import sys  # Runtime error prevention
sys.setrecursionlimit(10000)    # Release the limit to 10000

T = int(input())    # testcase

B, ck = [[]], [[]]  # [], [] : also possible

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]


def dfs(x, y):
    global B, ck
    ck[x][y] = 1
    for i in range(4):
        xx, yy = x + dx[i], y + dy[i]
        if B[xx][yy] is 0 or ck[xx][yy]:
            continue
        dfs(xx, yy)


def process():
    global B, ck
    M, N, K = map(int, input().split())
    # init field, +2 : fill the border with 0
    B = [[0 for i in range(M+2)] for _ in range(N+2)]
    ck = [[0 for i in range(M+2)] for _ in range(N+2)]
    for _ in range(K):
        X, Y = map(int, input().split())
        B[Y+1][X+1] = 1  # +1 : border wad added 1

    ans = 0
    for i in range(1, N+1):
        for j in range(1, M+1):
            if B[i][j] is 0 or ck[i][j]:
                continue
            dfs(i, j)
            ans += 1
    print(ans)


for _ in range(T):
    process()
###########################################################
sys.setrecursionlimit(100000)


def dfs(x, y):
    visited[x][y] = True
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if array[nx][ny] and not visited[nx][ny]:
            dfs(nx, ny)


for _ in range(int(input())):
    m, n, k = map(int, input().split())
    array = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]

    for _ in range(k):
        y, x = map(int, input().split())
        array[x][y] = 1
    result = 0

    for i in range(n):
        for j in range(m):
            if array[i][j] and not visited[i][j]:
                dfs(i, j)
                result += 1

    print(result)
