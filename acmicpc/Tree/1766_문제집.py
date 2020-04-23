import heapq

n, m = map(int, input().split())
array = [[] for i in range(n+1)]
indegree = [0] * (n+1)  # init degree to 0
heap = []

for _ in range(m):
    x, y = map(int, input().split())
    array[x].append(y)  # Create edge between nodes
    indegree[y] += 1    # increase edge

for i in range(1, n+1):
    if indegree[i] == 0:    # i means 'y' with no connection
        heapq.heappush(heap, i)

result = []

# Topological Sort
while heap:
    data = heapq.heappop(heap)
    result.append(data)
    for y in array[data]:
        indegree[y] -= 1    # delete one edge
        if indegree[y] == 0:    # like line 15
            heapq.heappush(heap, y)

for i in result:
    print(i, end=' ')
