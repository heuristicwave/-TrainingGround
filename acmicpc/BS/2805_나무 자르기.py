# 왜 이진 탐색일까? => 문제에 속아 넘어가지말자 멀리보면 같은 문제!
# 공유기 : 거리를 이진으로 파악
# 예산 : 평균을 이진으로 접근
# 나무 자르기 : max값의 반을 문제의 H로 반영하여 total을 아까처럼 진행

n, m = map(int, input().split())
trees = list(map(int, input().split()))

trees.sort()

start = 0
end = trees[-1]
result = 0

while start <= end:
    mid = (start+end) // 2
    get_trees = 0
    for i in range(n):
        tree = trees[i] - mid
        if tree < 0:
            tree = 0
        get_trees += tree

    if get_trees >= m:
        start = mid+1
        result = mid
    else:
        end = mid-1

print(result)
