def maxDifference(nums):
    diff = 0
    minNum = nums[0]

    for i in range(1, len(nums)):
        if nums[i] - minNum > diff:
            diff = nums[i] - minNum
        if nums[i] < minNum:
            minNum = nums[i]

    # err
    if diff is 0:
        diff = -1

    return diff