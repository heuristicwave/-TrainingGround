'''
x, y에서 시작했을 때 dist 만큼 상하좌우로 이동하여 몇칸을 확보 할 수 있는지 체크하여 max 출력
BFS + 재귀로 접근, DFS로 접근하면 상에서 방문 후 체크한곳이 다른곳의 진로를 방해하여
dist마다(level or depth 마다), 방문할 수 있는 위치를 큐에 넣고 점검한다

Error Handling
- 큐의 위치 : 전역 => getSpread 내부
=> 큐를 getSpread 들어갈때 마다 재생성 하지 않으면, update되면서 이전 위치를 기억 하지 못함
- 일반 bfs 처럼 while문 조건에 q를 넣으면 안됨, => bfs+재귀
- cnt, dist, visited check 위치에 따라 결과값 달라짐, 어디서 증가 시킬지 고려!!
'''
import copy

N, d = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(N)]

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
answer = 0


def getSpread(x, y, dist):
    # print('enter', x, y, dist)    # debug
    global cnt
    if dist > d:
        return 0

    q = deque()
    q.append((x, y))

    x, y = q.pop()

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if V[nx][ny] == 0:
                q.append((nx, ny))
                cnt += 1
                V[nx][ny] = 1

    while q:
        x, y = q.pop()
        getSpread(x, y, dist+1)

    return 0


for i in range(N):
    for j in range(N):
        x, y = i, j
        if B[x][y] is 1:
            continue
            # 매번 체크(visited) 배열을 다르게 유지해야 하기 때문에 B로 부터 복사
        V = copy.deepcopy(B)  # deep copy
        V[x][y] = 1
        cnt = 1
        getSpread(x, y, 1)
        # print('@@@@@ ret @@@@@ : ', cnt)	# for debug
        if answer < cnt:
            answer = cnt

print(answer)
