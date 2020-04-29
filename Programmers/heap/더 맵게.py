# heapify & auto sort & counter exam
import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)  # initialize

    # heapify implement
    # data = []
    # for s in scoville:
    #     heapq.heappush(data, s)

    while len(scoville) > 1:
        if scoville[0] >= K:
            return answer
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        combine = first+(second*2)
        heapq.heappush(scoville, combine)

        answer += 1

    # Counterexample : TC16
    if len(scoville) == 1:
        if scoville[0] >= K:
            return 1

    return -1


################### Best Solution ###################

# import heapq as hq

def solution(scoville, K):

    hq.heapify(scoville)
    answer = 0
    while True:
        first = hq.heappop(scoville)
        if first >= K:  # Improved time complexity
            break
        if len(scoville) == 0:
            return -1
        second = hq.heappop(scoville)
        hq.heappush(scoville, first + second*2)
        answer += 1

    return answer
