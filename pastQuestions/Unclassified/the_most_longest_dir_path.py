# Using BFS
from collections import deque


def solution(N, relation, dirname):
    adj = [[] for _ in range(N+1)]
    visited = [False] * (N+1)

    for i in relation:
        u, v = i[0], i[1]
        adj[u].append(v)
        adj[v].append(u)

    def bfs():
        temp = 0
        q = deque([(1, 0)])

        while q:
            d, cnt = q.popleft()
            #print('start', d, cnt)
            if not visited[d]:
                cnt += 1
                cnt += len(dirname[d-1])
                visited[d] = True
                #print('enter', d, cnt)
                for e in adj[d]:
                    if not visited[e]:
                        q.append((e, cnt))

                if cnt > temp:
                    temp = cnt
        return temp-1   # 마지막 / 제거

    return bfs()

# Using DFS


def solution(N, relation, dirname):
    answer = []

    adj = [[] for _ in range(N+1)]
    visited = [False] * (N+1)

    for i in relation:
        u, v = i[0], i[1]
        adj[u].append(v)
        adj[v].append(u)

    def dfs(v, s):
        s += 1  # / 길이 +1
        s += len(dirname[v-1])
        visited[v] = True

        for e in adj[v]:
            if not visited[e]:
                dfs(e, s)
        answer.append(s)

    for j in range(1, N+1):    # root 부터 시작
        if not visited[j]:
            dfs(j, 0)

    return max(answer)-1    # 맨마지막 / 길이 빼기
