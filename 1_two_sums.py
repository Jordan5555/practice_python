"""

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.


Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

"""

# Problem similar to 167:


'Solution 1:'


def twoSum(numbers, target):

    # Iterate through the list with index i
    for i in range(len(numbers) - 1):

        # Iterate through the list with index j, starting from the next element after i
        for j in range(i + 1, len(numbers)):

            # Check if the sum of numbers at indices i and j equals the target
            if numbers[i] + numbers[j] == target:

                # If yes, return the indices as a list [i, j]
                return [i, j]
            
    # If no such pair is found, return an empty list []
    return []



'Solution 2:'


def twoSum(numbers, target):

   
    # Initialize an empty dictionary to store numbers and their indices
    num_to_index = {}
    
    # Iterate over the list with index i and value num
    for i, num in enumerate(numbers):

        # Calculate the complement that would add up to the target with num
        complement = target - num
        
        # Check if the complement is already in the dictionary
        if complement in num_to_index:

            # If yes, return the indices of the complement and the current number
            return [num_to_index[complement], i]
        
        # If the complement is not found, add the current number and its index to the dictionary
        num_to_index[num] = i
    
    # If no such pair is found, return an empty list
    return []



'Solution 3:'


def twoSum(numbers, target):

    # Create a list of tuples (number, index) from the input list 'numbers'
    # and sort it by the number. This helps in applying the two-pointer technique.
    sorted_numbers = sorted((num, i) for i, num in enumerate(numbers))
    
    # Initialize two pointers: 'head' starting from the beginning (0)
    # and 'tail' starting from the end (len(sorted_numbers) - 1)
    head = 0
    tail = len(sorted_numbers) - 1
    
    # Loop until the 'head' pointer is less than the 'tail' pointer
    while head < tail:

        # Calculate the sum of the numbers at the 'head' and 'tail' pointers
        sum = sorted_numbers[head][0] + sorted_numbers[tail][0]
        
        # If the sum is less than the target, move the 'head' pointer to the right
        if sum < target:
            head += 1

        # If the sum is greater than the target, move the 'tail' pointer to the left
        elif sum > target:
            tail -= 1

        # If the sum equals the target, return the original indices of the numbers
        else:
            return [sorted_numbers[head][1], sorted_numbers[tail][1]]
    
    # If no pair is found that sums to the target, return an empty list
    return []

# Example usage:
print(twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]