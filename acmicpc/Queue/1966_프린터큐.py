test_case = int(input())

for _ in range(test_case):
    n, m = list(map(int, input().split(' ')))
    queue = list(map(int, input().split(' ')))
    # (i, idx) : index is tuple second element
    queue = [(i, idx) for idx, i in enumerate(queue)]

    # print(queue)
    # tc_1 : [(5, 0)]
    # tc_2 : [(1, 0), (2, 1), (3, 2), (4, 3)]
    # tc_3 : [(1, 0), (1, 1), (9, 2), (1, 3), (1, 4), (1, 5)]

    count = 0
    while True:
        # queue front == the most priority document
        # ==> If the most important thing is in front
        if queue[0][0] == max(queue, key=lambda x: x[0])[0]:
            count += 1
            # queue[0][1] <= [1] : index
            if queue[0][1] == m:
                print(count)
                break
            else:
                # print(queue) # [(4, 3), (1, 0), (2, 1), (3, 2)]
                queue.pop(0)  # del queue[0]
                # print(queue) # [(1, 0), (2, 1), (3, 2)]

        else:
            queue.append(queue.pop(0))
