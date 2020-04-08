tc = int(input())

# Create 2 stacks and have a cursor between them
for _ in range(tc):
    left_stack = []
    right_stack = []
    data = input()

    for i in data:
        if i == '-':
            if left_stack:
                left_stack.pop()
        elif i == '<':
            if left_stack:
                right_stack.append(left_stack.pop())
        elif i == '>':
            if right_stack:
                left_stack.append(right_stack.pop())
        else:
            left_stack.append(i)
    # extend : Insert element of list, tuple, dictionary
    # reverse right stack !!
    left_stack.extend(reversed(right_stack))

    print(''.join(left_stack))
