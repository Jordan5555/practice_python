"""


You are given an array nums consisting of positive integers.

Return the total frequencies of elements in nums such that those elements all have the maximum frequency.

The frequency of an element is the number of occurrences of that element in the array.

 

Example 1:

Input: nums = [1,2,2,3,1,4]
Output: 4
Explanation: The elements 1 and 2 have a frequency of 2 which is the maximum frequency in the array.
So the number of elements in the array with maximum frequency is 4.
Example 2:

Input: nums = [1,2,3,4,5]
Output: 5
Explanation: All elements of the array have a frequency of 1 which is the maximum.
So the number of elements in the array with maximum frequency is 5.
 

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100


"""


'Solution 1: '


def countMostFrequentNumbers(nums):
    
    """
    Counts the occurrences of each number in the list and returns the sum of the counts
    of the numbers that have the highest frequency.

    :param nums: List of integers.
    :return: Sum of the counts of the most frequently occurring numbers.
    """
    
    # Dictionary to store the frequency of each number
    frequency_dict = {}

    # Iterate through each number in the list and update its frequency in the dictionary
    for num in nums:
        frequency_dict[num] = frequency_dict.get(num, 0) + 1

    # Find the maximum frequency among all the numbers
    max_frequency = max(frequency_dict.values())

    # Sum the counts of the numbers that have the maximum frequency
    result = sum(count for count in frequency_dict.values() if count == max_frequency)

    return result



'Solution 2: '

from collections import Counter

def countMostFrequentNumbers(nums):
    """
    Counts the occurrences of each number in the list and returns the sum of the counts
    of the numbers that have the highest frequency.

    :param nums: List of integers.
    :return: Sum of the counts of the most frequently occurring numbers.
    """
    
    # Create a Counter object to count occurrences of each number
    counter = Counter(nums)
    
    # Find the maximum frequency among all numbers
    max_frequency = counter.most_common(1)[0][1]
    
    # Sum the counts of numbers that have the maximum frequency
    result = sum(count for num, count in counter.items() if count == max_frequency)
    
    return result




