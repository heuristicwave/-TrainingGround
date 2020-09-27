from collections import Counter


def usingCounter(s):
    answer = []
    array = list(map(str, s[2:-2:].split('},{')))

    for i in array:
        extract_num = map(int, i.split(','))
        answer += extract_num

    c = Counter(answer)

    return sorted(c, key=lambda x: c[x], reverse=True)


def usingMyCounter(s):
    answer = []

    # s1 = s.lstrip('{').rstrip('}').split('},{')
    array = list(map(str, s[2:-2:].split('},{')))

    for i in array:
        extract_num = map(int, i.split(','))
        answer += extract_num

    count = {}
    for i in answer:
        try:
            count[i] += 1
        except:
            count[i] = 1

    return sorted(count, key=lambda x: count[x], reverse=True)


'''
dict 정렬 하기 : https://blog.naver.com/msyang59/220627524714

또 다른 방법
groupby = list(set(answer))
result = dict()
for ip in groupby:
    result[ip] = answer.count(ip)
print(result)
'''
