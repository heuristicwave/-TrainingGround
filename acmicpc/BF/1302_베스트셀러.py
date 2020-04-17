n = int(input())

books = {}

for _ in range(n):
    book = input()

    if book in books:
        books[book] += 1
    else:
        books[book] = 1

bestSeller = max(books.values())
array = []

# params !!!!!!!!
for key, value in books.items():
    if value == bestSeller:
        array.append(key)

print(sorted(array)[0])
