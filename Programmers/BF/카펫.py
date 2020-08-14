def solution(brown, yellow):
    answer = []

    for i in range(1, yellow+1):
        if yellow % i == 0:
            vertical = i
            horizontal = int(yellow / i)
            if (vertical + horizontal) * 2 + 4 == brown:
                # if vertical > horizontal:
                #     vertical, horizontal = horizontal, vertical
                # answer.append(horizontal+2)
                # answer.append(vertical+2)
                # break
                return [max(vertical, horizontal)+2, min(vertical, horizontal)+2]

    return answer
