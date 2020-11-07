# 코드 출처 : https://velog.io/@seovalue

from itertools import permutations


def calc(numbers, operator):
    answer = numbers[0]
    for n, op in zip(numbers[1:], operator):
        if op == '+':
            answer += n
        elif op == '*':
            answer *= n
        elif op == '-':
            answer -= n
        elif op == '/':
            if answer < 0:  # 음수를 양수로 나눌 때
                answer = -1 * (abs(answer) // n)
            else:
                answer //= n
    return answer


n = int(input())
numbers = list(map(int, input().split()))
num_of_op = list(map(int, input().split()))
sample_op = ['+', '-', '*', '/']
operator = []

for i, j in zip(sample_op, num_of_op):
    print(i, j)
    if j >= 1:  # 연산자의 개수가 1이상이면, 개수만큼 operator에 삽입
        for _ in range(j):
            operator.append(i)

permutation_list = list(set((permutations(operator, len(operator)))))
answer = []
for p in permutation_list:
    answer.append(calc(numbers, p))

print(max(answer))
print(min(answer))
