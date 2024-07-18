"""

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 

The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. 

The remaining elements of nums are not important as well as the size of nums.

Return k.


Example 1:

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).


Example 2:

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).

Constraints:

0 <= nums.length <= 100
0 <= nums[i] <= 50
0 <= val <= 100

"""


'Solution 1:'


def remove_elem(nums, val):
    
	# Loop as long as val is present in nums
    while val in nums:  
        
		# Remove the first occurrence of val from nums
        nums.remove(val) 

	# Return the modified nums list
    return nums  



'Solution 2:'


def remove_elem(nums, val):
    
	# Initialize index to 0
    index = 0  
    
	# Loop while index is less than the length of nums
    while index < len(nums): 

		# Check if the element at index is equal to val
        if nums[index] == val: 

			# If equal, remove the element at index from nums
            nums.pop(index) 
             
        else:
            
			# If not equal, move to the next index
            index += 1  

	# Return the modified nums list
    return nums  


print(remove_elem(([2,2,1,3,0]), 2))
