'''
문제는 맞췄지만, 내 의도대로 100% 완벽한 코드는 아님
TC맞췄을 때, 4~5가 아니라 4~6이됨
결과적으로 길이를 1만큼 작게 구해서
end가 6까지 간것을 자동으로 5까지 간것으로 조정
'''
N, M = map(int, input().split())
data = list(map(int, input().split()))

min_len = N+1
interval_sum = 0
end = 0

for start in range(N):
    while interval_sum < M and end < N:
        interval_sum += data[end]
        # print('end/sum', end, interval_sum)
        end += 1
    if interval_sum >= M:
        length = end - start
        if length < min_len:
            min_len = length

    interval_sum -= data[start]

print(min_len if min_len < N+1 else 0)
