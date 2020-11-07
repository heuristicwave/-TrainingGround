# 양방향, 단방향 구분!!! => 이문제는 A <- B 방향
from collections import deque

n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]

for _ in range(m):      # [[], [3], [3], [4, 5], [], []]
    x, y = map(int, input().split())
    adj[y].append(x)    # A <- B


def bfs(v):
    q = deque([v])
    visited = [False] * (n+1)
    visited[v] = True
    count = 1
    while q:
        v = q.popleft()
        for e in adj[v]:
            if not visited[e]:
                q.append(e)
                visited[e] = True
                count += 1

    return count


result, max_value = [], -1

for i in range(1, n+1):
    c = bfs(i)
    if c > max_value:
        result = [i]
        max_value = c
        # print(f'result:{result} / max_value{max_value}')
    elif c == max_value:
        result.append(i)
        max_value = c
        # print(f'2: result:{result} / max_value{max_value}')

# print(" ".join(map(str, result)))
for e in result:
    print(e, end=" ")

################## !!! 시 간 초 과 !!! ##################
'''
a -> b, a -> c, b -> c
방문 체크를 하지 않기체 c를 중복 체크
'''


def bfs2(start):
    q = deque()
    q.append(start)
    visited = [False] * (n + 1)

    cnt = 1
    while q:
        v = q.popleft()
        visited[v] = True
        for i in adj[v]:
            if not visited[i]:
                q.append(i)
                cnt += 1
    return cnt
