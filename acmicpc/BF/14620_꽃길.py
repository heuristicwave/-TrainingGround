N = int(input())
G = [list(map(int, input().split())) for i in range(N)]
# c = [[0]*N for i in range(N)]

ans = 3000  # Maximum rental price
dx, dy = [0, 0, 1, 0, -1], [0, 1, 0, -1, 0]  # stay + 4way


def ck(lst):
    ret = 0
    flowerPot = []
    for flower in lst:
        # !! Key Point 1 !!
        # ex : location - 35, x => 5, y => 5 (5, 5)
        x = flower // N
        y = flower % N
        if x == 0 or x == N-1 or y == 0 or y == N-1:
            return 3000

        for w in range(5):
            flowerPot.append((x+dx[w], y+dy[w]))    # insert tuple
            ret += G[x+dx[w]][y+dy[w]]

    # !! Key Point 2 !!
    # If the pots are separated from each other, they have 15 positions.
    # The number below 15 is when the flower dies.
    if len(set(flowerPot)) != 15:
        return 3000
    return ret


# Brute-Force
for i in range(N*N):               # flower 1
    for j in range(i+1, N*N):      # flower 2
        for k in range(j+1, N*N):  # flower 3
            ans = min(ans, ck([i, j, k]))

print(ans)
