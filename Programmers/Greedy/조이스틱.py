def solution(name):
    answer, index = 0, 0
    name = list(name)

    while(True):
        right, left = 1, 1

        if name[index] != 'A':
            updown = min(ord(name[index])-ord('A'),
                         (ord('Z')-ord(name[index])+1))
            answer += updown

        name[index] = 'A'
        if name == ["A"]*len(name):
            break

        for i in range(1, len(name)):
            if name[index+i] == "A":
                right += 1
            else:
                break
        for i in range(1, len(name)):
            if name[index-i] == "A":
                left += 1
            else:
                break

        if right > left:
            answer += left
            index -= left
        else:
            answer += right
            index += right
    return answer


def solution2(name):
    answer, index = 0, 0
    name = list(name)
    name_len = len(name)

    # 위 아래 조작해서 A 맞추는거 횟수
    # ord(A) : 65, ord(Z) : 90 ex) 77까지 12, 78까지 13, 79까지 - 12
    for i in name:
        gap = ord(i) - 65
        if gap > 13:
            gap = 26 - gap
        answer += gap

    while(True):
        right, left = 1, 1

        name[index] = 'A'
        if name == ["A"] * name_len:
            break

        for i in range(1, name_len):
            if name[index+i] == "A":
                right += 1
                # print(f'right:{right}, idx+i :{index+i}, {name}')
            else:
                break
        for i in range(1, name_len):
            if name[index-i] == "A":
                left += 1
                # print(f'left:{left}, idx+i :{index+i}, {name}')
            else:
                break
        if right > left:
            answer += left
            index -= left
        else:
            answer += right
            index += right
    return answer
