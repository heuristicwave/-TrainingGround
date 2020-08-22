def dfs(numbers, target, cur_num, depth):
    total = 0

    if depth == len(numbers):
        if cur_num == target:
            return 1    # count++
        else:
            return 0

    # depth same as index order
    total += dfs(numbers, target, cur_num+numbers[depth], depth+1)
    total += dfs(numbers, target, cur_num-numbers[depth], depth+1)

    return total


def solution(numbers, target):
    answer = dfs(numbers, target, 0, 0)
    return answer
