# 백트래킹 - 조건을 만족하는 모든 조합의 수를 살펴봄

N, M = map(int, input().split())
A = [input().rstrip() for _ in range(N)]


def bfs():
    answer = 0
    q = set()   # 동일한 경우 한번만 계산하기 위해서
    q.add((0, 0, A[0][0]))  # 좌측 상단에서 시작

    while q:
        x, y, step = q.pop()
        answer = max(answer, len(step))

        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and A[nx][ny] not in step:
                q.add((nx, ny, step+A[nx][ny]))

    return answer


print(bfs())
