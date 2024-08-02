"""

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 

The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. 

The remaining elements of nums are not important as well as the size of nums.

Return k.


Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).


Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).


Link to check: 

https://youtube.com/watch?v=oMr9lehS7Us 
https://www.youtube.com/watch?v=DEJAZBq0FDA


"""


'Solution 1:'



def removeDuplicates(nums):

    # Initialize index i to 0
    i = 0
    
    # Iterate through the list 'nums' using a while loop
    while i < len(nums) - 1:
        
        # Check if the current element is equal to the next element
        if nums[i] == nums[i + 1]:
            
            # If duplicate found, remove the next element using pop()
            nums.pop(i + 1)
            
        else:
            # If no duplicate, move to the next element
            i += 1
    
    # Return the length of the modified 'nums' list
    return len(nums)




'Solution 2:'


def removeDuplicates(nums):


	# Initialize left pointer to index 0
    left = 0  
    
	# Initialize right pointer to index 1
    right = 1  
    
	# Loop until the right pointer reaches the end of the list
    while right < len(nums): 
        
		# Check if the elements at left and right pointers are equal
        if nums[left] == nums[right]:  
            
			# If equal, remove the element at right pointer index
            nums.pop(right) 
             
        else:
            
			# If not equal, update the left pointer to the right pointer
            left = right  

			# Increment the right pointer to move to the next element
            right += 1  
	
	# Return the length of the modified list
    return len(nums)  



'Solution 3:'


def removeDuplicates(nums):

	# same as in ex-27.	
	# Initialize index k to 0
	k = 0  

	# Iterate through each element x in the list nums
	for x in nums:            

		# Check if k is 0 or if x is not equal to the previous element
		if k == 0 or x != nums[k - 1]: 
                
			# Update the element at index k in nums to x
			nums[k] = x  
               
			# Increment k to move to the next position
			k += 1  

	# Return a slice of nums containing only the first k elements
	return nums[:k]  



print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
