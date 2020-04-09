# 서울에서 김서방 찾기
def solution(seoul):
    answer = ''
    answer = seoul.index("Kim")
    return "김서방은 {}에 있다".format(answer)

# k번째수


def solution(array, commands):
    answer = []
    cut = []
    comNum = len(commands)

    for i in range(comNum):
        a = commands[i][0]
        b = commands[i][1]
        c = commands[i][2]
        cut = array[a-1:b]
        cut.sort()
        answer.append(cut[c-1])
    return answer
