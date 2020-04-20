# In PyPy3 에서는 성공 Python3는 시간초과

import heapq

n = int(input())
heap = []
result = []

for _ in range(n):
    data = int(input())
    if data == 0:
        if heap:  # 존재 시, pop
            result.append(heapq.heappop(heap))
        else:
            result.append(0)
    else:
        heapq.heappush(heap, data)  # put data in heap

for data in result:
    print(data)
