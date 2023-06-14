"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order."""

# input = nums = [2,7,11,15], target = 9
# output = [0,1]
# explanation = nums[0] + nums[1] == 9, we return [0,1]

# loop over to get the first number
# loop and get the second number
# if num[0] and num[1] == target
# return the indices


def twoSum(lst, target):

    for i in range(0, len(lst)):
        for j in range(0, len(lst)):
            if lst[i] + lst[j] == target:
                return i, j


print(twoSum([2, 7, 11, 15], 9))
