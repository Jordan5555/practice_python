"""

Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
Note that the integers in the lists may be returned in any order.

 

Example 1:

Input: nums1 = [1,2,3], nums2 = [2,4,6]
Output: [[1,3],[4,6]]
Explanation:
For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].
For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums2. Therefore, answer[1] = [4,6].
Example 2:

Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2]
Output: [[3],[]]
Explanation:
For nums1, nums1[2] and nums1[3] are not present in nums2. Since nums1[2] == nums1[3], their value is only included once and answer[0] = [3].
Every integer in nums2 is present in nums1. Therefore, answer[1] = [].
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
-1000 <= nums1[i], nums2[i] <= 1000

"""

'Solution 1:'

def findDifference(nums1, nums2):
	
	l1 = []
	l2 = []

	# Find elements in nums1 that are not in nums2
	for num in nums1:
		if num not in nums2 and num not in l1:
			l1.append(num)

	# Find elements in nums2 that are not in nums1
	for num in nums2:
		if num not in nums1 and num not in l2:
			l2.append(num)

	return [l1, l2]



'Solution 2:' 


def findDifference(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    
    l1 = list(set1 - set2)  # Elements in set1 but not in set2
    l2 = list(set2 - set1)  # Elements in set2 but not in set1
    
    return [l1, l2]



print(findDifference([1,2,3], [2,4,6]))