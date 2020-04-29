# !! POINT !!
# Accumulated use amount => DP !!!
# Date parsing


def convert_day(x, y):
    month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = 0
    for i in range(x-1):
        day += month[i]
    day += y
    return day


def solution(purchase):
    answer = [0, 0, 0, 0, 0]  # rank

    date, money = [], []
    length = len(purchase)

    for i in range(length):
        x, y = purchase[i].split()
        date.append(x)
        money.append(int(y))

    for i in range(0, length):    # convert yymmdd => day
        y, m, d = map(int, date[i].split('/'))
        date[i] = convert_day(m, d)

    dp = [0] * (365+1)
    for i in range(length):
        for j in range(date[i], date[i]+30):    # dp : 0 ~ 30 day
            dp[j] += money[i]

    for i in range(1, len(dp)):  # count
        total = dp[i]
        if total >= 100000:
            answer[4] += 1
        elif total >= 50000:
            answer[3] += 1
        elif total >= 20000:
            answer[2] += 1
        elif total >= 10000:
            answer[1] += 1
        else:
            answer[0] += 1

    return answer
