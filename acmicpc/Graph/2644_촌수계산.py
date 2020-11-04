'''
양쪽으로 연결하기
deque에 튜플 넣는 방법
bfs count를 튜플로 전달해서 reset 시키는 효과
형제끼리 이동을 +2 촌이 아닌, 부모를 걸쳐서 확인했기 때문에 +1촌
'''

from collections import deque

N = int(input())
family = [[] for _ in range(N+1)]

A, B = map(int, input().split())
M = int(input())

for _ in range(M):
    x, y = map(int, input().split())    # x : parent, y : child
    family[x].append(y)
    family[y].append(x)  # 양쪽으로 연결 !!

checked = [False] * (N+1)


def bfs(start, target):
    count = 0
    q = deque([(start, count)])  # tuple을 []로 감싸서 deque에 넣기

    while q:
        person, count = q.popleft()

        if person == target:
            return count
        if not checked[person]:
            count += 1  # +1촌
            checked[person] = True

            for child in family[person]:    # 부모의 자식들 순회
                if not checked[child]:
                    q.append((child, count))
    return -1


print(bfs(A, B))
