'''
다중 조건 정렬
- 비교할 요소가 복수 개일 경우, 해당 순서를 튜플로 묶어 진행
'''

import re


def solution(files):
    # + : 여러개의 숫자를 기준으로, () : 숫자를 포함하여 split
    temp = [re.split(r"[0-9]+", s) for s in files]
    print(temp)
    # x[0](head)를 기준으로 정렬하고, x[1](number)을 기준으로 정렬
    sort = sorted(temp, key=lambda x: (x[0].lower(), int(x[1])))

    return ["".join(s) for s in sort]
