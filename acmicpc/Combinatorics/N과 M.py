from itertools import combinations_with_replacement  # 중족 조합
from itertools import product                        # 중복 순열
from itertools import combinations                   # 조합
from itertools import permutations                   # 순열


N, M = map(int, input().split())
A = [i for i in range(1, N+1)]

# 15649 : A중 M개로 가능한 순열
# >>> (1, 2) (1, 3)
for i in permutations(A, M):
    print(' '.join(map(str, list(i))))

# 15650 : A중 M개로 가능한 조합
for i in combinations(A, M):
    print(' '.join(map(str, list(i))))


# 15651 : 중복 순열, 자기 자신 포함하여 A중 M개로 가능한 순열
# >>> (1, 1) (1, 2) (1, 3) (1, 4) (2, 1) (2, 2) (2, 3) (2, 4)
for i in product(A, repeat=M):
    print(' '.join(map(str, list(i))))

# 15652 : 중복 조합
# >>> (1, 1) (1, 2) (1, 3) (1, 4) (2, 2) (2, 3) (2, 4) (3, 3) (3, 4) (4, 4)
for i in combinations_with_replacement(A, M):
    print(' '.join(map(str, list(i))))

# 15654 : 순열 오름차순 출력
for i in sorted(permutations(A, M)):
    print(' '.join(map(str, list(i))))

# 15655 : 조합 출력시 앞,뒤 바꿔서 출력
# !! 리스트 sort 먼저함 !!
# >>> (1 7), (1 8) (1 9) (7 8) (7 9) (8 9)
for i in combinations(sorted(A), M):
    print(' '.join(map(str, list(i))))

# 15656 : 중복 순열, 자기 자신 포함하여 A중 M개로 가능한 순열를 역순으로
for i in product(sorted(A), repeat=M):
    print(' '.join(map(str, list(i))))

# 15657 : 중복 조합, 역순으로
# >>> : (1 1) (1 7) (1 8) (1 9) (7 7) (7 8) (7 9) (8 8) (8 9) (9 9)
for i in combinations_with_replacement(sorted(A), M):
    print(' '.join(map(str, list(i))))
