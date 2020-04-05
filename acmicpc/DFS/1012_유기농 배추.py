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
