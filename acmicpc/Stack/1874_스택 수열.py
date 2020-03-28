n = int(input())

cp = 1  # couter point
stack = []
result = []

for i in range(1, n+1):
    data = int(input())

    while cp <= data:
        stack.append(cp)
        cp += 1
        result.append('+')
    if stack[-1] is data:
        stack.pop()
        result.append('-')
    else:
        print('NO')
        exit(0)

print('\n'.join(result))
