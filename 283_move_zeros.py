"""

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1


"""


'Solution 1:'


def moveZeroes(nums):

    # Initialize a pointer to keep track of the position to place non-zero elements
    insert_pos = 0
    
    # Iterate through the list
    for num in nums:

        if num != 0:

            # If the current number is not zero, move it to the current insert position
            nums[insert_pos] = num
            
            insert_pos += 1
    
    # After placing all non-zero elements, fill the rest of the list with zeros
    for i in range(insert_pos, len(nums)):
        nums[i] = 0
    
    return nums



'Solution 2:'


def moveZeroes(nums):

    # Loop through each element in the list, except the last one
    for i in range(len(nums) - 1):
        
        # For each element, loop through the subsequent elements
        for j in range(i + 1, len(nums)):
            
            # If the current element is zero
            if nums[i] == 0:
                
                # Swap the current element with the subsequent non-zero element
                nums[i], nums[j] = nums[j], nums[i]

    # Return the modified list        
    return nums  



'Solution 3:'


def moveZeroes(nums):

    # Initialize the left pointer to the start of the list
    left = 0  
    
    # Iterate through the list with the right pointer
    for right in range(len(nums)):
        
        # Check if the current element is non-zero
        if nums[right] != 0:
            
            # Only swap elements if left and right pointers are different
            if left != right:

                # Swap the current non-zero element with the element at the left pointer
                nums[left], nums[right] = nums[right], nums[left]
            
                # Move the left pointer to the right
                left += 1


print(moveZeroes([0,1,0,3,12]))
