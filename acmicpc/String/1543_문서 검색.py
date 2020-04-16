# 그리디, 문자열, 탐색
# 문서의 길이 2500, 단어길이 50 => O(NM)

document = input()
word = input()

index = 0
result = 0

while len(document) - index >= len(word):
    if document[index:index+len(word)] == word:
        result += 1
        index += len(word)
    else:
        index += 1

print(result)
