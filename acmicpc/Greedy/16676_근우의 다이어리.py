# 1 Pack : 10   (<11)
# 2 Pack : 110  (<111)
# 3 Pack : 1110 (<1111)

n = input()
s = '1'*len(n)

if len(n) == 1:
    print(1)
elif int(n) >= int(s):
    print(len(n))
else:
    print(len(n)-1)
