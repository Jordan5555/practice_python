"""

Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
 

Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105

Link to check: https://www.youtube.com/watch?v=BHr381Guz3Y


"""


def rotate(nums, k):
    # Calculate the effective rotation amount (handle cases where k >= len(nums))
    k = k % len(nums)
    
    # Rotate the list to the right by k positions
    nums[:] = nums[-k:] + nums[:-k]
    
    return nums


def rotatearray(nums, k):
    # Calculate the effective rotation amount (handle cases where k >= len(nums))
    k = k % len(nums)

    # Helper function to reverse elements in the array from index 'left' to 'right'
    def helper(left, right):
        while left < right:

            # Swap the elements at index 'left' and 'right'
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        return nums

    # Step 1: Reverse the entire array
    left = 0
    right = len(nums) - 1
    rotate = helper(left, right)

    # Step 2: Reverse the first k elements
    left = 0
    right = k - 1
    rotate = helper(left, right)

    # Step 3: Reverse the remaining elements from k to the end of the array
    left = k
    right = len(nums) - 1
    rotate = helper(left, right)

    # Return the rotated array
    return rotate

# Test the function with an example
print(rotatearray(nums = [1, 2, 3, 4, 5, 6, 7], k = 3))










