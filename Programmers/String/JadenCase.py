# capitalize() : 문자열의 첫글자는 대문자로, 나머지는 소문자로 변환
# title()로 JadenCase 한번에 해결 가능


def solution(s):
    answer = ''
    s = s.lower()
    A = s.split(" ")
    for word in A:
        word = word.capitalize()
        answer += word + " "

    return answer[0:-1]
