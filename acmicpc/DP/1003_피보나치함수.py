zero, one = [1, 0, 1], [0, 1, 1]


def fibo(num):
    length = len(zero)
    if length <= num:
        for i in range(length, num + 1):
            zero.append(zero[i - 1] + zero[i - 2])
            one.append(one[i - 1] + one[i - 2])
    print("%d %d" % (zero[num], one[num]))


for _ in range(int(input())):
    fibo(int(input()))
