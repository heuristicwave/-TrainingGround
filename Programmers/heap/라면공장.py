# 왜 우선순위일까? <= 나의 여유분 날짜 안에서 우선순위 최대를 선택
# while문 만들기 조건 stock < k
# 최소, 최대 일때 부호관리!

import heapq as hq


def solution(stock, dates, supplies, k):
    answer = 0
    idx = 0
    pq = []
    # stock + dates[answe만큼] >= k - 1
    while stock < k:
        for i in range(idx, len(dates)):
            if stock < dates[i]:
                break
            hq.heappush(pq, -supplies[i])   # max_heap(-), min_heap(+)
            idx = i + 1

        stock += hq.heappop(pq) * -1    # input(-)*output(-) => +
        answer += 1

    return answer
