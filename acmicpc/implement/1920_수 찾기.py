# !!! Time Out !!!

# N = input()
# A = list(map(int, input().split(" ")))
# M = input()
# B = list(map(int, input().split(" ")))

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

# A 부분을 쪼개서 int로 받은다음 있다면 1로 바꿈
# 없는 수는 참조 못하고 error
N, A = int(input()), {i: 1 for i in map(int, input().split(" "))}
M = input()

for i in list(map(int, input().split())):
    print(A.get(i, 0))  # 새로 입력받아 참조대상에 없으면 0으로 채움
    # print(1 if i in A else 0)
