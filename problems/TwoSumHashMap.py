def two_sum(nums, target):
    if type(nums) is not list:
        return []

    for i, num in enumerate(nums):
        if target - num in nums:
            return [target - num, i]

    return []
