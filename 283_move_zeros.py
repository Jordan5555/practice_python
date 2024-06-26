# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

 

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]
 

# Constraints:

# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1


# def func(lst, num):
# 	for i in lst:
# 		if i == num:
# 			lst.remove(i)
# 			lst.append(i)

# 	return lst



# def moveZeroes(nums):

#   left = 0

#   for right in range(len(nums)):

#     if nums[right] != 0:

#       nums[right], nums[left] = nums[left], nums[right]

#       left += 1

#   return nums


# [1,3,12,0,0]

def moveZeroes(nums):
    
    left = 0

    for right in range(len(nums)):
        
        if nums[right] != 0:
            
            nums[right], nums[left] = nums[left], nums[right]
            
            left += 1


    # for i in range(len(nums)-1):
        
    #     for j in range(i+1, len(nums)):

    #         if nums[i] == 0:

    #             nums[i], nums[j] = nums[j], nums[i]
                
    # return nums



    #   for i in range(len(nums)-1):
    #     if nums[i] == 0:
    #         nums.append(0)
    #         nums.remove(nums[i])

    # return nums

    return nums    

print(moveZeroes([0,1,0,3,12]))
