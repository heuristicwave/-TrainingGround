N, M = map(int, input().split())
before = [list(map(int, list(input()))) for _ in range(N)]
after = [list(map(int, list(input()))) for _ in range(N)]
answer = 0


def flip(x, y, before):
    for i in range(3):
        for j in range(3):
            before[x+i][y+j] ^= 1    # XOR OP, 0 <-> 1


for i in range(N-2):     # 3*3 이니까 뒤에 2개는 볼필요 없음
    for j in range(M-2):
        if before[i][j] != after[i][j]:
            flip(i, j, before)
            answer += 1

if before != after:
    print(-1)
else:
    print(answer)
# short code
# print(answer if before == after else -1)
