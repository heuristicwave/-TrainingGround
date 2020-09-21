import copy

'''
!! Point !!
조합 기능을 qry라는 check 배열로 검사하며 진행
DFS
백트레킹
'''

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
Q = [tuple(map(int, input().split())) for _ in range(K)]
answer = 5000  # 100 * 50


def value(arr):
    return min([sum(i) for i in arr])


def convert(arr, qry):
    (r, c, s) = qry
    r, c = r-1, c-1
    new_arr = copy.deepcopy(arr)
    # 1 0 -1 0 / 0, -1, 0, 1
    for i in range(1, s+1):
        rr, cc = r-i, c+i
        for x, y in (1, 0), (0, -1), (-1, 0), (0, 1):
            for d in range(i*2):
                rrr, ccc = rr + x, cc + y
                new_arr[rrr][ccc] = arr[rr][cc]
                rr, cc = rrr, ccc
    return new_arr


def dfs(arr, qry):
    print(qry)
    global answer
    if sum(qry) == K:   # query를 다 처리 했을때, 모두 1로 바뀌어 완료 시점이됨
        answer = min(answer, value(arr))
        return
    for i in range(K):
        if qry[i]:  # 처리된 것은 continue
            continue
        new_arr = convert(arr, Q[i])
        qry[i] = 1
        dfs(new_arr, qry)
        qry[i] = 0


# K개수 만큼 False가 들어간 리스트를 넘김
dfs(A, [0 for i in range(K)])   # [0] * K
print(answer)
