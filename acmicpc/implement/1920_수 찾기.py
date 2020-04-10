# !!! Time Out !!!

# N, A = int(input()), list(map(int, input().split()))
# M, B = int(input()), list(map(int, input().split()))

# result = []
# for i in range(len(B)):
#     if B[i] in A:
#         result.append(1)
#     else:
#         result.append(0)

# for i in result:
#     print(i, end='\n')

# For String
# print('\n'.join(result))

# Using set
# !! set is hash based, so it is faster than list !!
n = int(input())
array = set(map(int, input().split()))
m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i in array:
        print('0')
    else:
        print('1')


# A 부분을 쪼개서 int로 받은 다음 있다면 1로 바꿈
# 없는 수는 참조 못하고 error
N, A = int(input()), {i: 1 for i in map(int, input().split(" "))}
M = input()

# !! Example !!
# print(f'A : {A}')
# >>> A : {4: 1, 1: 1, 5: 1, 2: 1, 3: 1}

# i가 입력받는 매개변수 역할
for i in list(map(int, input().split())):
    print(A.get(i, 0))  # 새로 입력받아 참조대상에 없으면 0으로 표시
    # print(1 if i in A else 0)

print(f'A : {A}')
