"""

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000
 

Constraints:

n == nums.length
1 <= k <= n <= 105
-104 <= nums[i] <= 104

"""


def findMaxAverage(nums, k):

    # Calculate the sum of the first subarray of length k
    current_sum = sum(nums[:k])
    
    # Initialize max_sum with the sum of the first subarray
    max_sum = current_sum
    
    # Iterate over the rest of the array starting from index k
    for i in range(k, len(nums)):
        
        # Update the current sum by adding the current element and subtracting the element k positions back
        current_sum += nums[i] - nums[i-k]
        
        # Update max_sum to be the maximum of current_sum and max_sum
        max_sum = max(current_sum, max_sum)
    
    # Return the maximum average by dividing max_sum by k
    return max_sum / k


print(findMaxAverage([1,12,-5,-6,50,3], 4))
