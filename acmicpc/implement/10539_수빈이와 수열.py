n = int(input())
listN = list(map(int, input().split(" ")))
sumList = []
originList = []

for i in range(len(listN)):
    sumList.append(listN[i]*(i+1))

originList.append(sumList[0])
for i in range(1, len(listN)):
    originList.append(sumList[i] - sumList[i-1])

for i in originList:
    print(i, end=' ')


################################################
N, B = int(input()), list(map(int, input().split(" ")))

A = [0 for i in range(B)]
A[0] = B[0]

for i in range(1, N):
    A[i] = (B[i]*(i+1) - sum(A))

for i in A:
    print(i, end=' ')
