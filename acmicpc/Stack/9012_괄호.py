N = int(input())
# \n을 제거하기 위해 rstrip()
A = [str(input().rstrip()) for _ in range(N)]

for PS in A:
    check = []
    for j in PS:
        if check:
            if check[-1] == j:
                check.append(j)
            else:
                if check[-1] == ')':
                    if j == '(':
                        check.append(j)
                        continue
                check.pop()
        else:
            check.append(j)

    # print(check)    # debug
    print('NO' if check else 'YES')
