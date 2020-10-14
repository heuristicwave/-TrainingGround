# 펠린드롬


def solution(n, m):
    answer = 0

    for num in range(n, m+1, 1):
        str_num = str(num)
        length = len(str_num)
        new_num = ''

        for i in range(length-1, -1, -1):
            new_num += str_num[i]

        if num == int(new_num):
            answer += 1

    return answer


# solution 1
s = 'abcde'
s_reverse = ''
for char in s:
    s_reverse = char + s_reverse

# solution 2
s = 'abcde'
s_list = list(s)
s_list.reverse()

# solution 3
s = 'abcde'
print(''.join(reversed(s)))
print(s[::-1])
