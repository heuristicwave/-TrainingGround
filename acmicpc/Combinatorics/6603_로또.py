'''
Error Handling
k의 type이 str 혹은 int에 따라 아래 결과가 다름
if k == '0' & if not k
'''
from itertools import combinations

while True:
    # input().strip().split(), strip() : 양쪽 \n 제거
    S = list(map(str, input().split()))
    k, S = S[0], S[1:]

    if k == '0':   # 마지막 줄 0
        break

    A = list(combinations(S, 6))
    for i in range(len(A)):
        print(' '.join(A[i]))
    '''
    => short code
    for case in combinations(S, 6):
        print(' '.join(case))
        
    만약 파싱 처음 단계에서 str => int 했다면 마지막에
    print(' '.join(map(str, case)) map으로 가능
    '''

    print()
