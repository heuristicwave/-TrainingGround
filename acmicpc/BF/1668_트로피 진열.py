n = int(input())

array = []
for _ in range(n):
    array.append(int(input()))

left, right = 0, 0
# left
max = -2147000000
for i in range(n):
    if array[i] > max:
        max = array[i]
        left += 1

# right
max = -2147000000
for i in range(n-1, -1, -1):
    if array[i] > max:
        max = array[i]
        right += 1

print(left)
print(right)

######### Another Solution #########
# Using ascending func, call origin & origin.reverse()


def ascending(array):
    now = array[0]
    result = 1
    for i in range(1, len(array)):
        if now < array[i]:
            result += 1
            now = array[i]
    return result
