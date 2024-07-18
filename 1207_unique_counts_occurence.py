"""

Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

 

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
 

Constraints:

1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000


"""

'Solution 1:'

def uniqueOccurrences(arr):

    # Dictionary to count the frequency of each element in the array
    freq = {}
    
    # Set to store the count of each frequency to check for uniqueness
    count = set()

    # Populate the frequency dictionary
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    # Check if each frequency is unique
    for num in freq.values():
        if num in count:

            # If the frequency is already in the set, return False
            return False
        
        # Add the frequency to the set
        count.add(num)

    # If all frequencies are unique, return True
    return True


'Solution 2:'

def uniqueOccurrences(arr):
    
    # Dictionary to count the frequency of each element in the array
    freq = {}
    
    # Populate the frequency dictionary
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    # Check if the frequencies are unique
    counts = set(freq.values())

    # If the number of unique frequencies equals the number of different elements, return True
    return len(counts) == len(freq)
