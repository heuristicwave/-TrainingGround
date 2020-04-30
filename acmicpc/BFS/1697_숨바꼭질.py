# deque can be inserted and deleted in front and back
from collections import deque


MAX = 100001
n, k = map(int, input().split())
array = [0] * MAX


def bfs():
    q = deque([n])
    while q:
        now_pos = q.popleft()   # left element pop
        if now_pos == k:
            return array[now_pos]
        for next_pos in (now_pos - 1, now_pos + 1, now_pos * 2):    # 3 cases
            # included and not visited
            if 0 <= next_pos < MAX and not array[next_pos]:
                array[next_pos] = array[now_pos] + 1
                q.append(next_pos)


print(bfs())

# deque([5])
# deque([4, 6, 10])
# deque([6, 10, 3, 5, 8])
# deque([10, 3, 5, 8, 7, 12])
# deque([3, 5, 8, 7, 12, 9, 11, 20])
# deque([5, 8, 7, 12, 9, 11, 20, 2])
# deque([8, 7, 12, 9, 11, 20, 2])
# deque([7, 12, 9, 11, 20, 2, 16])
# deque([12, 9, 11, 20, 2, 16, 14])
# deque([9, 11, 20, 2, 16, 14, 13, 24])
# deque([11, 20, 2, 16, 14, 13, 24, 18])
# deque([20, 2, 16, 14, 13, 24, 18, 22])
# deque([2, 16, 14, 13, 24, 18, 22, 19, 21, 40])
# deque([16, 14, 13, 24, 18, 22, 19, 21, 40, 1])
# deque([14, 13, 24, 18, 22, 19, 21, 40, 1, 15, 17, 32])
# deque([13, 24, 18, 22, 19, 21, 40, 1, 15, 17, 32, 28])
# deque([24, 18, 22, 19, 21, 40, 1, 15, 17, 32, 28, 26])
# deque([18, 22, 19, 21, 40, 1, 15, 17, 32, 28, 26, 23, 25, 48])
# deque([22, 19, 21, 40, 1, 15, 17, 32, 28, 26, 23, 25, 48, 36])
# deque([19, 21, 40, 1, 15, 17, 32, 28, 26, 23, 25, 48, 36, 44])
# deque([21, 40, 1, 15, 17, 32, 28, 26, 23, 25, 48, 36, 44, 38])
# deque([40, 1, 15, 17, 32, 28, 26, 23, 25, 48, 36, 44, 38, 42])
# deque([1, 15, 17, 32, 28, 26, 23, 25, 48, 36, 44, 38, 42, 39, 41, 80])
# deque([15, 17, 32, 28, 26, 23, 25, 48, 36, 44, 38, 42, 39, 41, 80, 0])
# deque([17, 32, 28, 26, 23, 25, 48, 36, 44, 38, 42, 39, 41, 80, 0, 30])
