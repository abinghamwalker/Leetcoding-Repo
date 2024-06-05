"""
1. Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
"""

def twoSum(nums, target):
    num_dict = {}
    for i, num in enumerate(nums):
        leftover = target - num
        print(num_dict)
        if leftover in num_dict:
            print(leftover)
            return [num_dict[leftover], i]
        num_dict[num] = i
    return []

print(twoSum([3,2,4], 6))