def solution(clothes):
    answer = 1
    dic = dict()

    for name, kind in clothes:
        if kind not in dic:
            dic[kind] = 1
        else:
            dic[kind] += 1

    for val in dic.values():
        answer *= (val + 1)

    return answer - 1
