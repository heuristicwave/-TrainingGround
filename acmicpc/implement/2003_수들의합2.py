'''
Two Pointer Algorithm
start, end 를 설정하고 end를 증가시키며,
조건에 달성하면 카운트하고 start를 옮긴다.
'''
N, M = map(int, input().split())
data = list(map(int, input().split()))

count = 0
interval_sum = 0
end = 0

for start in range(N):  # list 대신 range를 설정해 인덱스 활용
    # 데이터의 범위를 벗어나지 않는 조건 설정
    while interval_sum < M and end < N:
        interval_sum += data[end]
        end += 1
    if interval_sum == M:
        count += 1
    interval_sum -= data[start]

print(count)