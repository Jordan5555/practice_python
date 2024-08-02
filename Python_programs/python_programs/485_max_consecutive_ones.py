"""

Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.

"""



'Solution 1:'

def findMaxConsecutiveOnes(nums):
    
    # Initialize variables to track the current count of consecutive ones and the maximum count found
    max_count = 0
    current_count = 0

    # Loop through each number in the list
    for num in nums:
        if num == 1:
            
            # If the current number is 1, increment the current count
            current_count += 1

            # Update the maximum count if the current count exceeds it
            max_count = max(max_count, current_count)

        else:
            
            # If the current number is not 1, reset the current count to 0
            current_count = 0

    return max_count


