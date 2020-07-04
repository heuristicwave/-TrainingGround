from itertools import permutations
import math


def check(n):
    k = math.sqrt(n)
    if n < 2:
        return False

    for i in range(2, int(k)+1):
        if n % i == 0:
            return False
    return True


def solution(numbers):
    answer = []

    for k in range(1, len(numbers)+1):
        # list(numbers)Pk
        perlist = list(map(''.join, permutations(list(numbers), k)))
        for i in list(set(perlist)):
            if check(int(i)):
                answer.append(int(i))

    answer = len(set(answer))

    return answer


# 아래처럼 하면 안됨 - 빼는 작업 중복으로 들어감 => set, 배열 활용
# import math

# def check(n):
#     end = int(math.sqrt(n))
#     for i in range(2, end+1):
#         if n % i == 0:
#             return False

#     return True

# def solution(n):
#     cnt = 1

#     for i in range(2, n+1):
#         if i % 2:   # 이거 추가해서 효율서 1, 3 통과
#             result = check(i)
#             if result:
#                 cnt += 1

#     return cnt

# range(2*i,n+1,i)
# i가 2일때, 2 배수 제거하기
# {2, 3, 4, 5, 6, 7, 8, 9, 10}
# {2, 3, 5, 7, 9}

# 효율성 200ms ~
def solution2(n):
    num = set(range(2, n+1))
    end = int(n ** 0.5)  # 제곱근 까지만 속도 개선 효율성 300ms -> 200ms
    for i in range(2, end+1):
        if i in num:
            num -= set(range(2*i, n+1, i))     # 해당 배수 제거

    return len(num)


# https://ychae-leah.tistory.com/190 효율성 100ms ~
def solution3(n):
    sieve = [True] * (n+1)

    m = int(n ** 0.5)
    for i in range(2, m + 1):            # n의 최대 약수가 sqrt(n) 이하
        if sieve[i] == True:             # i가 소수인 경우
            for j in range(2*i, n+1, i):  # i이후 i의 배수들을 False 판정
                sieve[j] = False

    return len([i for i in range(2, n+1) if sieve[i] == True])  # len()으로 개수 반환
