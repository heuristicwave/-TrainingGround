# simplify string : 0001100 => 010
# find rules
# 0, 1 : 0
# 01, 10 : 1
# 101, 010 : 1
# 1010 : 2
# 10101 : 2
# 101010 : 3

S, tot = input(), 0
# Key Point : Find changing section
for i in range(1, len(S)):
    if S[i] != S[i-1]:
        tot += 1

print((tot+1)//2)
