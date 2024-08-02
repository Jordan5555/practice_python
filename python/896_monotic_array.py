"""

An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise.

 

Example 1:

Input: nums = [1,2,2,3]
Output: true
Example 2:

Input: nums = [6,5,4,4]
Output: true
Example 3:

Input: nums = [1,3,2]
Output: false
 

Constraints:

1 <= nums.length <= 105
-105 <= nums[i] <= 105

"""

'Solution 1: '


def isMonotonic(nums):
    return nums == sorted(nums) or nums == sorted(nums, reverse=True)



'Solution 2: '


from itertools import pairwise


def isMonotonic(nums):

    # Check if all pairs (a, b) satisfy a <= b
    is_increasing = all(a <= b for a, b in pairwise(nums))
    
    # Check if all pairs (a, b) satisfy a >= b
    is_decreasing = all(a >= b for a, b in pairwise(nums))
    
    # Return True if either is_increasing or is_decreasing is True, indicating monotonicity
    return is_increasing or is_decreasing



'Solution 3:'


def isMonotonic(nums):

    # Initialize flags for increasing and decreasing
    increasing = decreasing = True
    
    # Iterate through the array starting from the second element
    for i in range(1, len(nums)):

        # Check if current element is less than previous
        if nums[i] < nums[i-1]:

            # If so, array is not strictly increasing
            increasing = False   
        
        # Check if current element is greater than previous
        if nums[i] > nums[i-1]:

            # If so, array is not strictly decreasing
            decreasing = False   
    
    # Return True if either increasing or decreasing is True, indicating monotonicity
    return increasing or decreasing


print(isMonotonic([1,2,3]))