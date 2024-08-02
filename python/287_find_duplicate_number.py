"""

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

 

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
Example 3:

Input: nums = [3,3,3,3,3]
Output: 3
 

Constraints:

1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.


"""


'Solution 1: Time Exceede Error'


def findDuplicate(nums):
    # Loop through each element with index1
    for index1 in range(len(nums)):
        # Loop through each element after index1 with index2
        for index2 in range(index1 + 1, len(nums)):
            # If a duplicate is found, return the element
            if nums[index1] == nums[index2]:
                return nums[index1]
    # If no duplicate is found, return False
    return False


'Solution 2:'


def findDuplicate(nums):
    seen = set()  # Create an empty set to keep track of seen numbers

    # Iterate through each number in the list
    for num in nums:
        # Check if the current number is already in the set
        if num in seen:
            # If yes, return the duplicate number
            return num
        # If no, add the current number to the set
        seen.add(num)

    # If no duplicates are found, return False
    return False


'Solution 3:'


def findDuplicate(nums):

    # Initialize an empty dictionary to track the frequency of numbers
    freq = {}  
    # Iterate through each number in the list
    for number in nums:
        # Check if the current number is already in the dictionary
        if number in freq:
            # If yes, return the duplicate number
            return number
        
        # If no, add the current number to the dictionary with a count of 1
        freq[number] = 1

    # If no duplicates are found, return False
    return False



'Solution 4:'


def findDuplicate(nums):
    # Iterate through each number in the list
    for number in nums:
        # Count the occurrences of the current number in the list
        # If the count is greater than 1, it means we have found a duplicate
        if nums.count(number) > 1:
            # Return the duplicate number
            return number

    # If no duplicates are found after iterating through the entire list, return False
    return False
