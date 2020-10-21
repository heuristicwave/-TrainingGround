def solution(record):
    answer, result = [], []
    db = {}

    for i in record:    # record 파싱
        temp = list(map(str, i.split()))
        answer.append(temp)

    for i in answer:    # record db에 삽입
        if i[0] == 'Enter':
            db[i[1]] = i[2]
        elif i[0] == 'Change':
            db[i[1]] = i[2]

    for i in answer:    # 최종 결과 확인해 result 저장
        if i[0] == 'Enter':
            result.append(db[i[1]]+'님이 들어왔습니다.')
        elif i[0] == 'Leave':
            result.append(db[i[1]]+'님이 나갔습니다.')

    return result
