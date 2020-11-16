'''
BitMask Sample

a = '1100'
a = int('0b'+a, 2)
print(a)
a >>= 1
print(bin(a))

문자열에 0을 채우는 방법
myStr.zfill(20)       >> 문자열 앞에 길이가 20이 되도록 0 채우기
myStr.ljust(20, '0')  >> 문자열 뒤에 길이가 20이 되도록 0 채우기, 이미 길이가 21이면 안됨
'''

# 런타임 해결못함

N, M = map(int, input().split())
train = ['0' * 20 for _ in range(N)]
orders = [list(map(int, input().split())) for _ in range(M)]

for order in orders:
    t_num = order[1] - 1
    if order[0] == 1:
        t_seat = order[2] - 1
        if train[t_num][t_seat] == '0':
            temp = int('0b' + train[t_num], 2)
            temp |= (1 << (20 - order[2]))
            train[t_num] = str(bin(temp)[2:]).zfill(20)
            # temp = list(train[t_num])
            # temp[t_seat] = '1'      # 승차
            # train[t_num] = ''.join(temp)
    elif order[0] == 2:
        t_seat = order[2] - 1
        if train[t_num][t_seat] == '1':
            temp = int('0b' + train[t_num], 2)
            temp &= ~(1 << (20 - order[2]))
            train[t_num] = str(bin(temp)[2:]).zfill(20)
            # temp = list(train[t_num])
            # temp[t_seat] = '0'      # 하차
            # train[t_num] = ''.join(temp)
    elif order[0] == 3:
        temp = int('0b' + train[t_num], 2)
        temp >>= 1
        train[t_num] = str(bin(temp)[2:]).zfill(20)
    elif order[0] == 4:
        temp = int('0b' + train[t_num], 2)
        temp <<= 1
        train[t_num] = str(bin(temp)[2:])[1:]

print(train)

check, answer = '', 0
for i in train:
    if i != check:
        answer += 1
    check = i
print(answer)
