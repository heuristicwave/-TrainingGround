# Key Point : mid값 기준 총합을 넘는지 못넘는지 비교

n, budget = int(input()), list(map(int, input().split()))
money = int(input())

start, end = 0, max(budget)  # Set up BS left, right
total_money = 0
result = 0

while start <= end:
    mid = (start+end) // 2
    total_money = 0

    # print(f'start:{start} / end:{end} / mid:{mid}')
    for i in budget:
        total_money += min(mid, i)
    # print(f'total_money:{total_money} / money:{money}')
    if total_money > money:  # over case
        end = mid - 1  # Move the end into the mid
    else:
        result = mid  # Key Point !!!!!!!!

        # Ability that guarantees the correct answer
        # start:123 / end:131 / mid:127 <== Answer
        # total_money:484 / money:485
        # start:128 / end:131 / mid:129 <== loop again
        # total_money:488 / money:485   <== but condition dissatisfaction
        # start:128 / end:128 / mid:128 <== loop again
        # total_money:486 / money:485   <== but condition dissatisfaction

        start = mid + 1  # Move the start out of the mid.

print(result)
