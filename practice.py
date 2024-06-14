# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true



def containsDuplicate(nums):

	nums.sort()

	i = 0

	while i < (len(nums)-1):

		if nums[i] == nums[i+1]:
			
			return True

		else:

			i += 1

	return False


print(containsDuplicate([1,2,3,1]))