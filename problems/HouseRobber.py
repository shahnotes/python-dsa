# https://leetcode.com/problems/house-robber

def rob_house(nums):
    rob, no_rob = 0, 0
    for num in nums:
        new_rob = no_rob + num
        new_no_rob = max(no_rob, rob)
        rob, no_rob = new_rob, new_no_rob
    return max(rob, no_rob)
