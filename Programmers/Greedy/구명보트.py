'''
요소의 삭제 없이, two pointer 적용
해당 알고리즘 그림
=> https://ducmanhphan.github.io/img/Algorithm/two-pointer/left-right-pointers.png  
'''


def solution(people, limit):
    answer = 0
    people.sort()
    first, end = 0, len(people)

    while first < end:
        if people[first] + people[end-1] <= limit:
            first += 1
            end -= 1
        else:
            end -= 1
        answer += 1

    return answer
