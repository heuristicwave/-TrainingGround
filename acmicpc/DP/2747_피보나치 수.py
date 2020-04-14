# def recursive(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return recursive(n) + recursive(n-1)

n = int(input())

a, b = 0, 1

while n > 0:
    a, b = b, a + b
    n -= 1

print(a)
