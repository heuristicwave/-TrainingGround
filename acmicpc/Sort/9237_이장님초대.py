'''
그림으로 그리면
day1, 4-0
day2, 4-1, 3-0
day3, 4-2, 3-1, 3-0
day4, 4-3, 3-2, 3-1, 2-0
day5, 4-4, 3-3, 3-2, 2-1
day6, end, end, 3-3, 2-2
day7, end, end, end, end

enumerate 사용하여 index와 day중 큰 값으로 갱신
'''
N = int(input())
A = sorted(list(map(int, input().split())), reverse=True)
answer = 0

for idx, day in enumerate(A):
    answer = max(answer, idx+day+2)

print(answer)
