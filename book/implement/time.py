import sys
import time

sys.stdin = open("input.txt", "r")
start = time.time()

N, cnt = int(input()), 0

# 00 00 00 ~ n 00 00
for hour in range(0, N+1):
    if '3' in str(hour):
        cnt += 3600
        continue
    for minute in range(0, 60):
        if '3' in str(minute):
            cnt += 60

            continue
        for second in range(0, 60):
            if '3' in str(second):
                cnt += 1
                continue

print(cnt)
print("time :", time.time() - start)
