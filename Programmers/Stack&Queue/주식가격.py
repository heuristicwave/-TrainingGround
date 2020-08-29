def solution(prices):
    length = len(prices)
    answer = [0] * length

    for i in range(length-1):
        for j in range(i, length-1):
            if prices[i] > prices[j]:
                break
            else:
                answer[i] += 1

    return answer
