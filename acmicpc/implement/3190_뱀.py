'''
!! Key Point !!
꼬리 위치 기억하는법
보드를 3가지 인자로 상태 표시하는것
'''
# Board, -1 : Snake / 0 : Empty / 1 : Apple
B = [[0] * 101 for _ in range(101)]
R = [0] * 10001  # Rotate
# 최대한 오래 버틴다고 가정할때, 문제조건 10000초 + 보드 100칸
SX, SY = [0] * 10101, [0] * 10101

N, K = int(input()), int(input())

for _ in range(K):
    x, y = map(int, input().split())
    B[x][y] = 1  # Put Apple

L = int(input())

for i in range(1, L+1):
    X, C = map(str, input().split())
    X = int(X)
    R[X] = C

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
T, dir = 0, 0    # 뱀이 처음 오론쪽 향하게 하기 위해 dir 0
x, y, = 1, 1
tail = T  # Point, tail이 시간만큼 움직였으니까 time 값 할당
SX[T], SY[T] = x, y
B[x][y] = -1    # start

while True:
    T += 1
    x, y = x + dx[dir], y + dy[dir]
    # 경계값 체크, 닿으면 종료
    if 1 > x or x > N or 1 > y or y > N or B[x][y] == -1:
        break
    SX[T], SY[T] = x, y

    if B[x][y] == 0:    # 꼬리 위치 재조정
        tx, ty = SX[tail], SY[tail]
        B[tx][ty] = 0
        tail += 1

    #print('x/y', x, y, B[1][8])
    B[x][y] = -1  # 뱀의 머리가 위치함
    if R[T] == 'D':
        dir = (dir+1) % 4
    if R[T] == 'L':
        dir = (dir+3) % 4

print(T)
