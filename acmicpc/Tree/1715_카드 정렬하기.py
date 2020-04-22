import heapq

heap = []
n = int(input())

for _ in range(n):
    heapq.heappush(heap, int(input()))

result = 0

while len(heap) != 1:
    first = heapq.heappop(heap)
    second = heapq.heappop(heap)
    combine = first + second
    result += combine
    heapq.heappush(heap, combine)
print(result)
