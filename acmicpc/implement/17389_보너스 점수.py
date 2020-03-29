N, S = int(input()), input()

bonus = 0
score = 0

for i in range(len(M)):
    if S[i] is 'X':
        bonus = 0
    else:
        score += (i+1)
        score += bonus
        bonus += 1

print(score)
####################################
## Another Solution ##

N, S = input(), input()

score, bonus = 0, 0

for idx, OXpointer in enumerate(S):
    if OXpointer == 'O':
        score, bonus = score + idx + 1 + bonus, bonus+1
    else:
        bonus = 0

print(score)
