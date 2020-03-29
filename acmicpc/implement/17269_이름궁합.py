N, M = map(int, input().split(" "))
first, second = input().split()

alp = [3, 2, 1, 2, 4, 3, 1, 3, 1, 1, 3, 1,
       3, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

# technic...
merge = ''
min_len = min(N, M)
for i in range(min_len):
    merge += first[i] + second[i]

merge += first[min_len:] + second[min_len:]

# ord(i)-ord('A') : matching index
lst = [alp[ord(i)-ord('A')] for i in merge]

for i in range(N+M-2):
    for j in range(N+M-1-i):
        lst[j] += lst[j+1]

print("{}%".format(lst[0] % 10*10 + lst[1] % 10))
