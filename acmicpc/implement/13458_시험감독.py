N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

answer = N
for i in A:
    if i < B:   # 한 교실 내에서 정감독관이 다 감독할 수 있으면 continue
        continue
    answer += (i - B)//C
    if (i - B) % C != 0:
        answer += 1

'''
for num in A:
    num -= B
    if num < 0:
        continue
    answer += num // C if num % C == 0 else num // C + 1
'''
print(answer)
