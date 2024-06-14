# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.


def majority(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums.sort()
    return nums[len(nums) // 2]
        


print(majority([2,2,3,3,3,3,3,3,1,1,1,2,2,2,3,3,3,3]))



