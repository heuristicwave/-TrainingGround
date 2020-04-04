S, tmp = input(), ""

ck = False

for i in S:
    if i == ' ':
        if not ck:
            # Print current word in reverse, put space at the end!!
            print(tmp[::-1], end=" ")
            tmp = ""  # like buffer flush
        else:
            print(" ", end="")
    elif i == '<':
        ck = True
        print(tmp[::-1] + i, end="")
        tmp = ""
    elif i == '>':
        ck = False
        print(i, end="")
    else:  # Print alphabet and number
        if ck:
            print(i, end="")
        else:
            tmp += i

print(tmp[::-1])


# Using Python Array[::] (https://blog.wonkyunglee.io/3)

# >> arr = range(10)
# >> arr[::2] # front to back, two step
# [0,2,4,6,8]
# >> arr[1::2] # front to back, start at index 1
# [1,3,5,7,9]
# >> arr[::-1] # print reverse, -1
# [9,8,7,6,5,4,3,2,1,0]
# >> arr[3::-1] # last to front, start at index 3
# [3,2,1,0]
# >> arr[1:6:2] # from index 1 to index 6, two step
# [1,3,5]
