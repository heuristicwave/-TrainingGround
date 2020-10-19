def solution(dartResult):
    temp, score = 0, []

    for i in dartResult:
        if 48 <= ord(i) <= 57:    # 0 <= i <=9
            if temp == 1 and ord(i) == 48:
                temp = 10
            else:
                temp = int(i)
            '''
            10을 k로 치환하여 해결
            dartResult = dartResult.replace('10','k')
            point = ['10' if i == 'k' else i for i in dartResult]
            '''

        if i == 'S':
            temp **= 1
            score.append(temp)
        elif i == 'D':
            temp **= 2
            score.append(temp)
        elif i == 'T':
            temp **= 3
            score.append(temp)
        '''
        index 함수를 활용한 풀이
        sdt = ['S', 'D', 'T']
        answer[i] = answer[i] ** (sdt.index(j)+1)
        '''

        if i == '*':
            num = len(score)
            if num == 1:
                score[0] *= 2
            elif num == 2:
                score[0] *= 2
                score[1] *= 2
            elif num == 3:
                score[1] *= 2
                score[2] *= 2
        '''
        고정값 3이 아닌 i로 진행했을 때
        if j == '*':
            answer[i] = answer[i] * 2
            if i != 0 :
                answer[i - 1] = answer[i - 1] * 2
        '''
        elif i == '#':
            score[-1] *= -1

    # print(score)  # debug

    return sum(score)
