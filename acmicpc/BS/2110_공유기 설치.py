# Binary Search => O(N*logX)
# Find the most gap, between houses

n, c = map(int, input().split())

array = []
for _ in range(n):
    array.append(int(input()))
array.sort()

start = array[1] - array[0]  # min distance
end = array[-1] - array[0]  # max distance
result = 0

while(start <= end):
    mid = (start + end) // 2    # gap between min and max
    value = array[0]
    count = 1

    # check distance, if select point is bigger than gap
    for i in range(1, len(array)):
        if array[i] >= value + mid:
            value = array[i]    # Update next start point
            count += 1          # Install router

    if count >= c:  # enable install router more than problem condition
        start = mid + 1
        result = mid    # Update the most gap => last result is answer
    else:   # disable install router more than problem condition
        end = mid - 1   # decrease gap

print(result)
