# min = 0, max = len(stones) => bs
def solution(stones, k):
    start, end = 1, max(stones) + 1

    while start < end - 1:
        mid = (start + end) // 2

        cnt, flag = 0, True
        temp_arr = stones

        for temp in temp_arr:
            if temp < mid:
                cnt += 1
            else:
                cnt = 0
            if cnt >= k:
                flag = False
                break

        if flag:
            start = mid
        else:
            end = mid

    return start
