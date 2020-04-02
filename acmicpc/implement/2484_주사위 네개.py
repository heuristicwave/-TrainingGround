N = int(input())

max = -2147000000


def money(lst):
    reward = 0
    if len(set(lst)) is 1:
        reward = 50000 + lst[0]*5000
    elif len(set(lst)) is 2:
        # 3 3 3 6 / 3 6 6 6
        if lst[1] is lst[2]:
            reward = 10000 + lst[1]*1000
        else:  # 3 3 6 6
            reward = 2000 + (lst[1] + lst[2]) * 500
    elif len(set(lst)) is 3:
        for i in range(3):
            if lst[i] is lst[i+1]:
                reward = 1000 + lst[i]*100
    else:
        reward = lst[3]*100
    return reward


# print(max(money() for i in range(N)))
for _ in range(N):
    lst = sorted(list(map(int, input().split())))
    reward = money(lst)
    if reward > max:
        max = reward

print(max)
