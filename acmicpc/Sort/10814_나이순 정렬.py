# Point
# Using tuple, set 'key attribute' sort by order

tc = int(input())

array = []
for _ in range(tc):
    input_data = input().split(' ')
    array.append((int(input_data[0]), input_data[1]))

# sort() : only list / sorted() all iterable(tuple, dictionary)
# The rest of the elements are stable
# ket=lambda parameter_list: expression
array = sorted(array, key=lambda x: x[0])   # based on first index

for i in array:
    print(i[0], i[1])
