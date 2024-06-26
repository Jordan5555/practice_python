# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.


# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.



# Problem similar to 167:

def twoSum(numbers, target):

    # index_map = {}

    # for index, num in enumerate(numbers):

    #     complement = target - num

    #     if complement in index_map:
    #         return (index_map[complement], index)
        
    #     index_map[num] = index

            
        # head = 0
        # tail = len(numbers)-1

        # while head <= tail:
            
        #     sum = numbers[head] + numbers[tail]

        #     if sum < target:
        #         head += 1

        #     elif sum > target:
        #         tail -= 1

        #     else:
        #         return [head, tail]
        
        # return [head, tail]



    # for i in range(len(nums)-1):
    #     for j in range(1, len(nums)):
    #         if nums[i] + nums[j] == target and i != j:
    #             return [i, j]