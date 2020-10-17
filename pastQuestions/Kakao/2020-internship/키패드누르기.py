def solution(numbers, hand):
    answer = ''
    # init position
    lpos = [1, 4]  # *
    rpos = [3, 4]

    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            answer += 'L'
            lpos = [1, (i-1)/3+1]    # 1열의 y좌표 보정을 위한 식
        elif i == 3 or i == 6 or i == 9:
            answer += 'R'
            rpos = [3, i/3]  # 3열은 3의 배수라 3으로 나눔

        else:   # 2열은 temp를 활용한 고정값 활용
            if i == 2:
                temp = [2, 1]
            if i == 5:
                temp = [2, 2]
            if i == 8:
                temp = [2, 3]
            if i == 0:
                temp = [2, 4]

            ldis = abs(temp[0]-lpos[0])+abs(temp[1]-lpos[1])
            rdis = abs(temp[0]-rpos[0])+abs(temp[1]-rpos[1])

            if ldis < rdis:
                answer += 'L'
                lpos = temp
            elif ldis > rdis:
                answer += 'R'
                rpos = temp
            else:
                if hand == "right":
                    answer += 'R'
                    rpos = temp
                else:
                    answer += 'L'
                    lpos = temp
    return answer
