"""

Given an array of positive integers nums, return an array answer that consists of the digits of each integer in nums after separating them in the same order they appear in nums.

To separate the digits of an integer is to get all the digits it has in the same order.

For example, for the integer 10921, the separation of its digits is [1,0,9,2,1].
 

Example 1:

Input: nums = [13,25,83,77]
Output: [1,3,2,5,8,3,7,7]
Explanation: 
- The separation of 13 is [1,3].
- The separation of 25 is [2,5].
- The separation of 83 is [8,3].
- The separation of 77 is [7,7].
answer = [1,3,2,5,8,3,7,7]. Note that answer contains the separations in the same order.
Example 2:

Input: nums = [7,1,3,9]
Output: [7,1,3,9]
Explanation: The separation of each integer in nums is itself.
answer = [7,1,3,9].
 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 105

"""

'Solution 1: '


def separateDigits(nums):
    
    # Using a list comprehension to iterate through each number in nums,
    # convert each digit of the number to an integer, and collect them in a list.
    return [int(digit) for number in nums for digit in str(number)]



'Solution 2:'


def func(nums):

    # Initialize an empty list to store individual digits
    out = []  

    # Iterate through each number in the list nums
    for i in nums:  

        # Convert the number to a string
        x = str(i)  

        # Iterate through each character (digit) in the string representation of the number
        for y in x:  

            # Append each digit to the list out
            out.append(int(y))

    # Return the list containing all digits
    return out  


print(separateDigits([13,25,83,77]))

