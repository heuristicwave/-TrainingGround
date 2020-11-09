a, b, c = map(int, input().split())
domino = [[] for _ in range(a+1)]
crash = [False] * (a+1)

for _ in range(b):
    pre, post = map(int, input().split())
    domino[pre].append(post)    # pre -> post 정방향 관계 설정

push_list = [int(input()) for _ in range(c)]

cnt = 0


def fall_down(pre):
    global cnt
    cnt += 1
    crash[pre] = True

    if len(domino[pre]) != 0:
        for i in domino[pre]:   # 쓰러트릴수 있는 도미노 확인해서 fall_down
            fall_down(i)


for i in push_list:
    if not crash[i]:    # 쓰러지지 않았다면 쓰러트림
        fall_down(i)

print(cnt)
