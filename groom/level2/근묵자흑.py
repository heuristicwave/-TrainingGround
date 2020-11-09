# Reference - https://gist.github.com/inspirit941/db8054cbffbb7c44299d8fde0e71c163

import math

n, k = map(int, input().split())
a = list(map(int, input().split(' ')))

min_pos = a.index(min(a))
answer = math.inf  # 부동소수점 양의 무한대

for i in range(k):
    left, right = a[:min_pos-i], a[min_pos+k-i:]
    left_cnt = len(left) // (k-1) + (1 if len(left) % (k-1) else 0)
    right_cnt = len(right) // (k-1) + (1 if len(right) % (k-1) else 0)
    answer = min(answer, 1 + left_cnt + right_cnt)

print(answer)
