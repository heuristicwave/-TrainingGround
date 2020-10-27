'''
nCr : 서로 다른 n개에서 순서를 생각하지 않고 r개를 뽑는 것
n! / r! * (n-r)!
'''
for _ in range(int(input())):
    N, M = map(int, input().split())

    answer = 1  # 동쪽과 서쪽의 사이트 갯수가 동일

    # nCr 구현
    if N != M:
        for i in range(M, M-N, -1):    # 분모와 약분 되는 것을 고려해 m-n 까지만
            print('Numerator', i)   # debug
            answer *= i
        for i in range(N, 1, -1):
            print('Denominator', i)  # debug
            answer //= i

    print(answer)
