def solution(n, lost, reserve):
    lost_num = len(lost)

    for i in lost:
        for j in reserve:
            # TC-12 Limitations 5, Example : 8, [4, 5], [5, 6], 7
            if i != j and (j in lost):
                continue
            if i - 1 == j or i + 1 == j or i == j:
                lost_num -= 1
                reserve.remove(j)
                break

    return n - lost_num
