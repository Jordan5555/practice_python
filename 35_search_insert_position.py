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


'Solution 1:'

def searchInsert(nums, target):

    # Check if target already exists in nums
    if target in nums:  

        # Return the index of target if found
        return nums.index(target)  
    
    # Iterate through nums
    for index in range(len(nums)): 

        # Find the first element >= target
        if nums[index] >= target: 

            # Return the index where target should be inserted
            return index  
    
    # If target is larger than all elements in nums, insert at the end
    return len(nums)  


    
'Solution 2:'


def searchInsert(nums, target):

    # If target is already in nums, return its index
    if target in nums:
        return nums.index(target)  

    # Two pointers
    left = 0
    right = len(nums) - 1

    # Perform binary search until left meets or exceeds right
    while left <= right:  

        # Calculate the middle index
        mid_point = (right + left) // 2 

        # Adjust the search range to the left of mid_point
        if nums[mid_point] > target:
            right = mid_point - 1  

        # Adjust the search range to the right of mid_point
        elif nums[mid_point] < target:
            left = mid_point + 1  

        # Return mid_point if target is found in nums
        else:
            return mid_point  

    # Return left index if target is not found, which indicates where target should be inserted
    return left  
