N, M = map(int, input().split())

answer = []
for i in range(N, M+1):
    narcissistic = 0
    for j in str(i):
        j = int(j)
        narcissistic += j*j*j
    if i == narcissistic:
        answer.append(i)

# 요소가 int 형일때 (str로 바꿔서 출력)
print(" ".join(map(str, answer)) + " ")
