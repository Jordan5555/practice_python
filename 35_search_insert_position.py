"""

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4


"""


def searchInsert(nums, target):

    
    # if target in nums:
    #     return nums.index(target)


    # for i in range(len(nums)):
    #     if nums[i] >= target:
    #         return i

    # return i+1


        
    # left = 0
    # right = len(nums)-1

    # if target in nums:
    #     return nums.index(target)

    # while left <= right:

    #     mid = left + (right - left) // 2

    #     if nums[mid] > target:
    #         right = mid - 1

    #     elif nums[mid] < target:
    #         left =  mid + 1

    #     else:
    #         return mid

    # return left
  


print(searchInsert([1,3,5,6], 2))