# 스킬이 중복해 주어지지 않으니까
# skill에 해당하는 문자만 추려서 비교


def solution(skill, skill_trees):
    answer = 0

    for user_skill in skill_trees:
        tmp = []

        for i in user_skill:
            if i in skill:
                tmp.append(i)
        flag = True

        for i in range(len(tmp)):
            # 첫번째 스킬로 시작하지 않는 것
            if tmp[i] != skill[i]:
                flag = False
                break

        if flag is True:
            answer += 1

    return answer
