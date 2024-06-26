# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. 

# You may assume that the majority element always exists in the array.

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
 

# Constraints:

# n == nums.length
# 1 <= n <= 5 * 104
# -109 <= nums[i] <= 109



# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2


def majority(nums):
    

    # nums.sort()
    # return nums[len(nums) // 2]


    # d = {}

    # for i in nums:
    #     d[i] = d.get(i, 0) + 1
    
    # return max(d, key = d.get)


    count = 0

    majority_element = None

    for number in nums:

        if count == 0:

            majority_element = number
            
            count = 1
        
        elif number == majority_element:

            count += 1

        else:

            count -= 1

    
    return majority_element
                


print(majority([2,2,1,0,-1,-1,-1]))



