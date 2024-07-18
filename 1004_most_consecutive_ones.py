"""

Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
0 <= k <= nums.length


 """


def longestOnes(nums, k):
        
    # Initialize the left and right pointers
    left_pointer = right_pointer = 0


    # Traverse the array while the right_pointer is within the array bounds
    while right_pointer < len(nums):

        # Decrease k when a '0' is encountered 
        if nums[right_pointer] == 0:
            k -= 1
            
        # If k is less than 0, slide the window to the right 
        # by moving the left_pointer to the next position
        if k < 0:

            # When we move the left_pointer forward, we need to check if 
            # we are passing over a '0' and if so, increase k
            if nums[left_pointer] == 0:
                k += 1

            # Move the left pointer to the right
            left_pointer += 1
            
        # Move the right pointer to the right
        right_pointer += 1
        
    # The length of the longest subarray of 1's (possibly with one flipped 0)
    # is the difference between the right and left pointers.
    return right_pointer - left_pointer

print(longestOnes([1,1,1,0,0,0,1,1,1,1,0], 1))