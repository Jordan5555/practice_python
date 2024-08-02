"""

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109

"""


'Solution 1:'


def containsDuplicate(nums):
    
    # Convert the list to a set. Sets automatically remove duplicates.
    nums_set = set(nums)
    
    # Compare the length of the set with the length of the original list.
    # If they are not the same, it means there were duplicates in the list.
    return len(nums_set) != len(nums)



'Solution 2:'


def containsDuplicate(nums):
    
    # Initialize an empty dictionary to store the frequency of each element
    frequency = {}

    # Iterate through each number in the list
    for num in nums:
        
        # If the number is already in the dictionary, a duplicate is found
        if num in frequency:
            return True
        
        # Otherwise, add the number to the dictionary
        frequency[num] = 1

    # If no duplicates are found, return False
    return False



'Solution 3:'


def containsDuplicate(nums):
    
    # Sort the list
    nums.sort()

    # Initialize index to 0
    i = 0

    # Iterate through the sorted list
    while i < (len(nums) - 1):
        
        # If the current element is equal to the next element, return True (duplicate found)
        if nums[i] == nums[i + 1]:
            return True
        
        else:
            
            # Move to the next element
            i += 1

    # If no duplicates are found, return False
    return False



'Solution 4: '


def func(nums):
    # Initialize a dictionary to keep track of the frequency of each number
    freq = {}

    # Iterate through each number in the list
    for num in nums:
        # Increment the frequency of the number
        freq[num] = freq.get(num, 0) + 1

    # Check if any number has a frequency of 1
    for count in freq.values():
        if count == 1:
            # If any number appears only once, return False
            return False

    # If all numbers appear more than once, return True
    return True


print(containsDuplicate([1,2,2,3]))