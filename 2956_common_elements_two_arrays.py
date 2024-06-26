# You are given two integer arrays nums1 and nums2 of sizes n and m, respectively. Calculate the following values:

# answer1 : the number of indices i such that nums1[i] exists in nums2.
# answer2 : the number of indices i such that nums2[i] exists in nums1.
# Return [answer1,answer2].

 

# Example 1:

# Input: nums1 = [2,3,2], nums2 = [1,2]

# Output: [2,1]

# Explanation:



# Example 2:

# Input: nums1 = [4,3,2,3,1], nums2 = [2,2,5,2,3,6]

# Output: [3,4]

# Explanation:

# The elements at indices 1, 2, and 3 in nums1 exist in nums2 as well. So answer1 is 3.

# The elements at indices 0, 1, 3, and 4 in nums2 exist in nums1. So answer2 is 4.

# Example 3:

# Input: nums1 = [3,4,2,3], nums2 = [1,5]

# Output: [0,0]

# Explanation:

# No numbers are common between nums1 and nums2, so answer is [0,0].

 

# Constraints:

# n == nums1.length
# m == nums2.length
# 1 <= n, m <= 100
# 1 <= nums1[i], nums2[i] <= 100



def findIntersectionValues(nums1, nums2):

  # a = 0
  # b = 0

  # for i in range(len(nums1)):
  #   if nums1[i] in nums2:
  #     a += 1
  
  # for j in range(len(nums2)):
  #   if nums2[j] in nums1:
  #     b += 1

  # return a,b

  # # Convert both lists to sets to remove duplicates and to allow for O(1) lookups
  #   set_nums1, set_nums2 = set(nums1), set(nums2)
  
  #   # Calculate the sum of elements in nums1 that are also in set_nums2
  #   # This counts the number of elements in nums1 present in the intersection
  #   intersection_count1 = sum(x in set_nums2 for x in nums1)
  
  #   # Calculate the sum of elements in nums2 that are also in set_nums1
  #   # This counts the number of elements in nums2 present in the intersection
  #   intersection_count2 = sum(x in set_nums1 for x in nums2)
  
  #   # The function returns a list with both counts as elements
  #   return [intersection_count1, intersection_count2]


  #  return [sum(n in nums2 for n in nums1), sum(n in nums1 for n in nums2)]


print(findIntersectionValues([4,3,2,3,1], [2,2,5,2,3,6]))