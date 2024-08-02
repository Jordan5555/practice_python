"""

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1

Explanation: 2 does not exist in nums so return -1
 

Constraints:

1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.


Link to check: https://www.youtube.com/watch?v=s4DPM8ct1pI


"""


'Solution 1: Same as 35'

def search(nums, target):

    # Check if target already exists in nums
    if target in nums:  

        # Return the index of target if found
        return nums.index(target) 

    # Initialize the left pointer to the start of the array
    left = 0

    # Initialize the right pointer to the end of the array
    right = len(nums) - 1
    
    # Continue searching while the left pointer is less than or equal to the right pointer
    while left <= right:

        # Calculate the middle index
        # mid = left + (right - left) // 2
        mid = (right + left) // 2 
        
        # If the middle element is less than the target, move the left pointer to mid + 1 to search the right half
        if nums[mid] < target:
            left = mid + 1

        # If the middle element is greater than the target, move the right pointer to mid - 1 to search the left half
        elif nums[mid] > target:
            right = mid - 1
            
        # If nums[mid] == target, return the index of the target
        else:
            return mid
    
    # Return -1 if the target is not found in the array
    return -1


print(search([-1,0,3,5,9,12], target = 9))