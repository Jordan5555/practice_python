"""

Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

 

Example 1:

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
Example 2:

Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
Example 3:

Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
 

Constraints:

n == nums.length
1 <= n <= 104
0 <= nums[i] <= n
All the numbers of nums are unique.

"""



'Solution 1:'

def missingNumber(nums):  

    # Iterate through the range from 0 to len(nums)
    for index in range(len(nums) + 1):

        # Check if the index is not in the nums list
        if index not in nums:

            # If the index is not found, return it as the missing number
            return index


'Solution 2:'

def missingNumber(nums):
    
    # Initialize result to the length of the nums list
    result = len(nums)
    
    # Iterate over each index and number in the list
    for i in range(len(nums)):

        # XOR result with the index and the number at that index
        result ^= i
        result ^= nums[i]
    
    # Return the result, which is the missing number
    return result


'Solution 3: '


def findMissingNumber(nums):
    """
    Given an array `nums` containing n distinct numbers taken from the range 0 to n,
    find the one number that is missing from the range.
    """

    # Initialize a variable to hold the total sum of numbers from 0 to n
    total = 0

    # Iterate over the range from 0 to n (inclusive)
    for i in range(len(nums) + 1):
        # Accumulate the sum of numbers from 0 to n
        total += i

    # Calculate the sum of all numbers in the input array `nums`
    array_sum = sum(nums)

    # The missing number is the difference between the total sum (0 to n) and the sum of the array
    return total - array_sum

# Example usage
nums = [3, 0, 1]
print(findMissingNumber(nums))  # Output: 2
