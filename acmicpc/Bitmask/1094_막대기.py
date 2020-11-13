'''
23일때 10111, 1의 갯수를 파악해야함

shift연산을 하면서 갯수 파악

10111 & 1 = 1 
101111 & 000001이라 마지막 자리만 연산
'''
X = int(input())
answer = 0

while X > 0:
    if X & 1:
        # print(bin(X), X & 1)
        answer += 1
    X >>= 1

print(answer)

# SHORT CORD, X의 2진값의 1의 갯수 출력
print(str(bin(int(input()))[2:]).count('1'))