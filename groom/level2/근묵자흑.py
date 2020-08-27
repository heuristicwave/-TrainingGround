n, m = map(int, input().split())
array = list(map(int, input().split(' ')))

min_element = min(array)
min_loc = array.index(min_element)

answer = 0

# 중복되는 min_loc 빼기, 중복처리 제대로 못함...
res_list = [i for i, value in enumerate(array) if value == min_element]
if len(res_list) > 1:
    answer -= len(res_list) - 1

left, right = 0, 0
if min_loc == m:
    right -= 1
while min_loc > 0:
    min_loc -= (m-1)
    left += 1

min_loc = array.index(min_element)
while min_loc < n:
    min_loc += (m-1)
    right += 1

print(answer + left + right)
