"""

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.


"""



def productExceptSelf(nums):
    # Initialize the output array where each element is 1
    product_array = [1] * len(nums)

    # Initialize left product to 1 (this will hold the cumulative product from the left)
    left_product = 1

    # First pass: calculate the left product for each element
    for i in range(len(nums)):

        # Assign the current left product to the output array
        product_array[i] = left_product

        # Update the left product by multiplying with the current number
        left_product *= nums[i]

    # Initialize right product to 1 (this will hold the cumulative product from the right)
    right_product = 1

    # Second pass: calculate the right product for each element, starting from the end
    for i in range(len(nums)-1, -1, -1):

        # Multiply the current element in the output array by the current right product
        product_array[i] *= right_product
        
        # Update the right product by multiplying with the current number
        right_product *= nums[i]

    return product_array
