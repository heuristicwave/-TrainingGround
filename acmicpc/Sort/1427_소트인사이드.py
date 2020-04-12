# Solve in a new way without built-in functions

# Matching 0 ~ 9, count num from 0 to 9
array = input()

for i in range(9, -1, -1):
    for j in array:
        if int(j) == i:
            print(i, end='')
