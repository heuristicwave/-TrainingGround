tc_str = str(input().rstrip())
length = len(tc_str)
words, suffix_array = [], []

# banana, anana, nana, ana, na, a
for front in range(length):
    word = tc_str[front:length]
    if word in words:
        continue
    else:
        words.append((word, front+1))

# a, ana, anana, banana, na, nana
words = sorted(words)

for word in words:
    suffix_array.append(word[1])

print(suffix_array)

answer, temp = [], []
temp = words[0]

for i in range(1, len(words)):
    if temp == words[i][0][0:len(temp)]:
        print(temp)
        temp = words[i][0]
