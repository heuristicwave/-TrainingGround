'''
딕셔너리 만들고 key, value 값 넣은 후,
value 기준으로 sort하여 key 값 출력
'''


def solution(N, stages):
    result = {}
    num = len(stages)

    for stage in range(1, N+1):
        if num != 0:
            count = stages.count(stage)
            result[stage] = count / num
            num -= count
        else:
            result[stage] = 0

    return sorted(result, key=lambda x: result[x], reverse=True)
