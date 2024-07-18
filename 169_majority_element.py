"""

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 

You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109



Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

"""


'Solution 1:'

def majority(nums):

    # Sort the list of numbers
    nums.sort()

    # Return the element at the middle index
    return nums[len(nums) // 2]  




'Solution 2:'

def majority(nums):

    # Dictionary to store frequencies of each number
    frequency = {}

    # Count occurrences of each number in nums
    for num in nums:
        frequency[num] = frequency.get(num, 0) + 1

    # Find the number with the highest frequency (majority element)
    return max(frequency, key=frequency.get)




'Solution 3: '


from collections import Counter


def func(nums):


    # Dictionary to store frequencies of each number
    freq = Counter(nums)

    
    # Find the number with the highest frequency (majority element)
    return freq.most_common(1)[0][0]




'Solution 4: Boyer-Moore Voting Algorithm'

def majority(nums):
    
    # Initialize variables to track the majority candidate and its count
    # Candidate for majority element
    candidate = None

    # Count of occurrences of candidate  
    count = 0         
    
    # Traverse through each number in the list
    for num in nums:
        if count == 0:

            # If count is 0, we need to choose a new candidate
            candidate = num
            count = 1

        elif num == candidate:

            # If current number is the same as candidate, increase count
            count += 1

        else:
            
            # If current number is different from candidate, decrease count
            count -= 1
    
    # The candidate variable now holds the majority element
    return candidate

                


print(majority([2,2,1,0,-1,-1,-1]))



