"""

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
 

Constraints:

n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.
 
"""

'Solution 1: '


def sortColors(nums):
    """
    Sorts the array nums in-place such that all 0s come first, 
    followed by all 1s, and then all 2s.
    """
    
    # Traverse the list and use a simple bubble sort approach
    for i in range(len(nums) - 1):

        # Compare each element with the elements after it
        for j in range(i + 1, len(nums)):
            
            # If the element at j is less than the element at i, swap them
            if nums[j] < nums[i]:
                # Perform the swap
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp


'Solution 2: '


def sortColors(nums):
    """
    Sorts the array nums in-place such that all 0s come first, 
    followed by all 1s, and then all 2s.
    """
    
    # Traverse the list and use a simple bubble sort approach
    for i in range(len(nums) - 1):
        # Compare each element with the elements after it
        for j in range(i + 1, len(nums)):
            # If the element at j is less than the element at i, swap them
            if nums[j] < nums[i]:
                # Perform the swap
                nums[i], nums[j] = nums[j], nums[i]
    return nums


'Solution 3: '


def sortColors(nums):
    """
    Sorts the array nums in-place such that all 0s come first, 
    followed by all 1s, and then all 2s.
    """
    
    # Pointers for the current element, and the boundaries of 0s and 2s
    current = 0
    p0 = 0
    p2 = len(nums) - 1
    
    # Traverse the list
    while current <= p2:
        if nums[current] == 0:
            # Swap the current element with the element at p0
            nums[current], nums[p0] = nums[p0], nums[current]
            # Increment the pointers for current and p0
            current += 1
            p0 += 1
        elif nums[current] == 2:
            # Swap the current element with the element at p2
            nums[current], nums[p2] = nums[p2], nums[current]
            # Decrement the pointer for p2
            p2 -= 1
        else:
            # Move to the next element
            current += 1

# Example usage
nums = [2, 0, 2, 1, 1, 0]
sortColors(nums)
print(nums)  # Output: [0, 0, 1, 1, 2, 2]

