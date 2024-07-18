"""

Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.

 

Example 1:

Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 5000
0 <= nums[i] <= 5000

"""

#On**2

def sortArrayByParity(nums): 
    
    if len(nums) == 1:

        return nums

    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] %2 != 0:
                nums[i], nums[j] = nums[j], nums[i]


    return nums[::-1]

print(sortArrayByParity([0,1]))


'Solution 1:'

def sortArrayByParity(nums):

    # Initialize two lists to store even and odd numbers separately
    even = []
    odd = []

    # Loop through each number in the input list
    for num in nums:

        # Check if the number is even
        if num % 2 == 0:

            # Append even numbers to the 'even' list
            even.append(num)

        else:

            # Append odd numbers to the 'odd' list
            odd.append(num)

    # Combine the 'even' and 'odd' lists, with even numbers first
    return even + odd


'Solution 2:'


def sortArrayByParity(nums):

    # Initialize the pointer for the position to place the next even number
    left = 0

    # Iterate through the list with the right pointer
    for right in range(len(nums)):

        # Check if the current number is even
        if nums[right] % 2 == 0:

            # Swap the even number with the number at the 'left' pointer
            nums[left], nums[right] = nums[right], nums[left]
            
            # Move the 'left' pointer to the right
            left += 1

    # The list is now sorted by parity, with all even numbers at the beginning
    return nums
