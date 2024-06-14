# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.


# Example 1:

# Input: nums = [2,2,1]
# Output: 1
# Example 2:

# Input: nums = [4,1,2,1,2]
# Output: 4
# Example 3:

# Input: nums = [1]
# Output: 1


# def singleNumber(self, nums: List[int]) -> int:
#         xor = 0
#         for num in nums:
#             xor ^= num

#         return xor 


def single_number(nums):

	d = {}

	for i in nums:

		d[str(i)] = d.get(i, 0) + 1

	return d


print(single_number([4, 1, 2, 1, 2]))
