N, answer = int(input()), 0
array = sorted([int(input()) for _ in range(N)])

# Using For Loop
# for i in range(1, N+1):
#     answer += abs(i - array[i-1])

for num, i in enumerate(array):
    answer += abs(num+1 - i)    # gap, between actual and expected

print(answer)
