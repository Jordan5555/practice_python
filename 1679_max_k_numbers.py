"""

You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.

 

Example 1:

Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.


Example 2:

Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total.+
 of 1 operation.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= k <= 109


"""


'Solution 1: '


def maxOperations(nums, k):
    # Sort the array in non-decreasing order
    nums.sort()

    # Initialize two pointers, head starting from the beginning, and tail from the end
    head = 0
    tail = len(nums) - 1

    # Initialize the count of operations
    count = 0

    # Loop until the two pointers meet
    while head < tail:
        # Calculate the sum of the elements pointed by head and tail
        sum = nums[head] + nums[tail]

        # If the sum equals k, increment the count and move both pointers
        if sum == k:
            count += 1
            head += 1
            tail -= 1

        # If the sum is greater than k, move the tail pointer to the left
        elif sum > k:
            tail -= 1

        # If the sum is less than k, move the head pointer to the right
        else:
            head += 1

    # Return the total count of operations
    return count



	# Same from 1 & 167
    
def maxOperations(nums, k):
    
    # Dictionary to store frequency of each number in nums
    freq = {}
    
    # Counter for the number of valid pairs
    count = 0

    # Iterate through each number in nums
    for num in nums:
        
        # Calculate the complement needed to sum up to k with num
        complement = k - num
        
        # Check if complement exists in freq and has a positive frequency
        if complement in freq and freq[complement] > 0:
            
            # Increment the count of valid pairs
            count += 1
            
            # Decrease the frequency of complement in freq
            freq[complement] -= 1
            
        else:
            
            # If complement doesn't exist in freq, add num with frequency 1
            if num in freq:
                freq[num] += 1
				
            else:
                freq[num] = 1

    # Return the total count of valid pairs
    return count


print(maxOperations(nums = [1,2,3,4], k = 5))