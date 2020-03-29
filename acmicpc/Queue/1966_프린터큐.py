test_case = int(input())

for _ in range(test_case):
    n, m = list(map(int, input().split(' ')))
    queue = list(map(int, input().split(' ')))
    # (i, idx) : index is tuple second element
    queue = [(i, idx) for idx, i in enumerate(queue)]

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
                queue.pop(0)  # line 20과 23의 차이 정확히!

        else:
            queue.append(queue.pop(0))
