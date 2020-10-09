for _ in range(int(input())):
    N, M = map(int, input().split())

    answer = 1  # 동쪽과 서쪽의 사이트 갯수가 동일할때
    if N != M:
        for i in range(M, M-N, -1):
            answer *= i
        for i in range(N, 1, -1):
            answer //= i

    print(answer)
