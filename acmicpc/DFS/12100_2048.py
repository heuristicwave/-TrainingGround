from copy import deepcopy

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]


def rotate90(B, N):
    NB = deepcopy(B)
    for i in range(N):
        for j in range(N):
            NB[j][N-i-1] = B[i][j]  # 90도 회전
    return NB


def convert(lst, N):
    # 0이 아닌 merge 대상들, 그냥 if i 쓰면 0은 걸러짐
    new_list = [i for i in lst if i != 0]
    for i in range(1, len(new_list)):
        if new_list[i-1] == new_list[i]:
            new_list[i-1] *= 2  # 같은거 2배
            new_list[i] = 0     # 전 값은 0으로
    # merge 이후 생긴 0제거, ex) 2,2,2 > 4,0,2 > 4,2
    new_list = [i for i in new_list if i]
    return new_list + [0] * (N-len(new_list))   # 나머지는 0으로 채움


def dfs(N, B, count):
    ret = max([max(i) for i in B])  # 보드 내에서 가장 큰 값
    if count == 0:
        return ret

    for _ in range(4):  # UP, DOWN, RIGHT, LEFT => rotate90 할때마다 방향 효과 얻음
        X = [convert(i, N) for i in B]    # 각 줄마다 새로운 줄을 만듬(갱신)
        if X != B:  # 같다면 더이상 처리 할 것이 없는것!, 다르면 한번 더
            ret = max(ret, dfs(N, X, count-1))
        B = rotate90(B, N)  # 다른방향 점검
    return ret


print(dfs(N, board, 5))
