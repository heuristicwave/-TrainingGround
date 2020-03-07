cnt = input()  # the number of testcase

# 반복횟수와 문자열을 받는다
for _ in range(int(cnt)):
    case = input()
    case = case.split()
    print(case[0], case[1])
    text = ''

    for c in case[1]:
        text += c*int(case[0])  # times

    print(text)
