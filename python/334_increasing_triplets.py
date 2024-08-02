"""

Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

 

Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
Example 3:

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
 

Constraints:

1 <= nums.length <= 5 * 105
-231 <= nums[i] <= 231 - 1

"""


'Solution: 1 - Gives error for this test case - [20,100,10,12,5,13]'


def increasingTriplet(nums):

    # Check if the length of nums is less than 3, which means it's impossible to have a triplet
    if len(nums) < 3:
        return False
    
    # Iterate through nums from index 1 to len(nums)-2
    for i in range(1, len(nums)-1):

        # Check if nums[i-1] < nums[i] < nums[i+1], indicating a triplet in strictly increasing order
        if nums[i-1] < nums[i] < nums[i+1]:
            return True
    
    # If no triplet in strictly increasing order is found, return False
    return False



'Solution 2:' 


def increasingTriplet(nums):

    # Initialize two variables to store the smallest and second smallest numbers found so far

    # Set first to infinity initially
    first = float('inf')   

    # Set second to infinity initially
    second = float('inf')  

    # Iterate through each number in the array
    for num in nums:
        
        if num <= first:

            # Update first if num is smaller or equal
            first = num  

        elif num <= second:

            # Update second if num is smaller or equal but larger than first
            second = num  

        else:

            # If num is larger than both first and second, we found an increasing triplet
            return True  

    # If no increasing triplet is found after iterating through the array
    return False  
