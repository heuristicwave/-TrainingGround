# bfs로 풀기 : https://myjamong.tistory.com/235

N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

visited = [False] * (N+1)
# print(adj)    # debug


def dfs(start):
    visited[start] = True

    for i in adj[start]:
        if not visited[i]:
            dfs(i)


cnt = 0
for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        cnt += 1
print(cnt)
