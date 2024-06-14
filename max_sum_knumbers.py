# 1679. Max Number of K-Sum Pairs
# Medium
# Topics
# Companies
# Hint
# You are given an integer array nums and an integer k.

# In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

# Return the maximum number of operations you can perform on the array.

 

# Example 1:

# Input: nums = [1,2,3,4], k = 5
# Output: 2
# Explanation: Starting with nums = c:
# - Remove numbers 1 and 4, then nums = [2,3]
# - Remove numbers 2 and 3, then nums = []
# There are no more pairs that sum up to 5, hence a total of 2 operations.
# Example 2:

# Input: nums = [3,1,3,4,3], k = 6
# Output: 1
# Explanation: Starting with nums = [3,1,3,4,3]:
# - Remove the first two 3's, then nums = [1,4,3]
# There are no more pairs that sum up to 6, hence a total of 1 operation.


def maxOperations(nums, k):	
	nums.sort()
	head = 0
	tail = len(nums)-1
	count = 0

	while head < tail:

		sum = nums[head] + nums[tail]

		if sum == k:
			count += 1
			head += 1
			tail -= 1 

		elif sum > k:
			tail -=1

		else:
			head += 1
			
	return count



print(maxOperations([1,2,3,4], 5))
