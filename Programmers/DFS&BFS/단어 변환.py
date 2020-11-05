from collections import deque


def cmpWord(cmp, tmp):
    cnt = 0
    for i in range(len(cmp)):
        if cmp[i] == tmp[i]:
            cnt += 1
    return cnt


def solution(begin, target, words):
    answer = -1
    if not target in words:
        return 0
    checked = [False] * len(words)

    q = deque()
    q.append((begin, answer))

    while q:
        cmp, ans = q.popleft()
        answer = ans
        answer += 1
        # print(cmp, answer)    # for debug
        if cmp == target:
            break
        for i in range(len(words)):
            if not checked[i]:
                tmp = words[i]
                ret = cmpWord(cmp, tmp)
                if ret == len(cmp)-1:
                    checked[i] = True
                    q.append((tmp, answer))

    return answer

###################### Wrong Answer ######################


def solution(begin, target, words):
    if not target in words:
        return 0

    checked = [False] * len(words)

    def dfs(word, depth):
        print(word, depth, checked)
        depth += 1
        if word == target:
            print('finish', depth)
            return depth

        for i in range(len(words)):
            if not checked[i]:
                cmp = words[i]
                cnt = 1
                for j in range(len(cmp)):
                    if cmp[j] == word[j]:
                        cnt += 1
                    if cnt == len(cmp):
                        checked[i] = True
                        dfs(cmp, depth)
                        # break   # list.remove(x): x not in list

        return depth
    return dfs(begin, 1)


'''
hit 1 [False, False, False, False, False, False]
hot 2 [True, False, False, False, False, False]
dot 3 [True, True, False, False, False, False]
dog 4 [True, True, True, False, False, False]

log 5 [True, True, True, False, True, False]
lot 6 [True, True, True, True, True, False]
lot 6 [True, True, True, True, True, False]
cog 6 [True, True, True, True, True, True]
finish 7
dog 4 [True, True, True, True, True, True]
'''
