"""

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
 

Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.

"""




'Solution 1:'


def func(nums):

    # Initialize an empty dictionary to store the frequency of each number
    frequency = {}

    # Iterate over each number in the list `t`
    for number in nums:
        # Update the frequency count of the number in the dictionary `d`
        # If the number is not in the dictionary, initialize it with 0 and add 1
        # If the number is already in the dictionary, increment its count by 1
        frequency[number] = frequency.get(number, 0) + 1

    # Find the key (number) in the dictionary `d` that has the minimum value (frequency)
    return min(frequency, key=frequency.get)




'Solution 2: '


def singleNumber(nums):

    # Initialize result to 0, as XORing with 0 will not change the result
    result = 0
    
    # Iterate over each number in the list
    for num in nums:
        # Apply XOR operation between result and the current number
        # This will cancel out pairs of the same number, leaving only the unique number
        result ^= num
    
    # Return the single unique number
    return result


print(singleNumber([4,1,2,1,2]))