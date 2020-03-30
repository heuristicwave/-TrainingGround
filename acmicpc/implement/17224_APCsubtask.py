N, L, K = map(int, input().split())

easy, hard = 0, 0

for i in range(N):
    sub1, sub2 = map(int, input().split())
    if sub2 <= L:
        hard += 1
    elif sub1 <= L:
        easy += 1

# print(100*easy + hard*140) # wrong answer
print(min(hard, K) * 140 + min(easy, K-hard)*100)
