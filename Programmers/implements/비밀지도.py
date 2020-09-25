def convert(num, n):
    binary = ''

    # bin쓰고 0b 붙는거 [2:]로 제거
    while num >= 1:
        binary += str(num % 2)
        num = num // 2

    while True:
        if len(binary) == n:
            break
        binary += '0'

    return binary[::-1]


def solution(n, arr1, arr2):
    answer = []
    board = [[0] * n for _ in range(n)]

    # zip 쓰면 더 좋아
    for i in range(n):
        arr1[i] = convert(arr1[i], n)
        arr2[i] = convert(arr2[i], n)

    for i in range(n):
        hashtag = ''
        for j in range(n):
            if int(arr1[i][j]) or int(arr2[i][j]):
                hashtag += '#'
            else:
                hashtag += ' '
        answer.append(hashtag)

    return answer
