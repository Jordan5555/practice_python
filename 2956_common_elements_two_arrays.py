"""

You are given two integer arrays nums1 and nums2 of sizes n and m, respectively. Calculate the following values:

answer1 : the number of indices i such that nums1[i] exists in nums2.
answer2 : the number of indices i such that nums2[i] exists in nums1.
Return [answer1,answer2].

 

Example 1:

Input: nums1 = [2,3,2], nums2 = [1,2]

Output: [2,1]

Explanation:



Example 2:

Input: nums1 = [4,3,2,3,1], nums2 = [2,2,5,2,3,6]

Output: [3,4]

Explanation:

The elements at indices 1, 2, and 3 in nums1 exist in nums2 as well. So answer1 is 3.

The elements at indices 0, 1, 3, and 4 in nums2 exist in nums1. So answer2 is 4.

Example 3:

Input: nums1 = [3,4,2,3], nums2 = [1,5]

Output: [0,0]

Explanation:

No numbers are common between nums1 and nums2, so answer is [0,0].

 

Constraints:

n == nums1.length
m == nums2.length
1 <= n, m <= 100
1 <= nums1[i], nums2[i] <= 100


"""

'Solution 1: '

def findIntersectionValues(nums1, nums2):
    """
    Finds the number of elements in nums1 that are also in nums2 and vice versa.

    :param nums1: List of integers.
    :param nums2: List of integers.
    :return: List of two integers [nums1_count, nums2_count].
    """

    # Initialize counters for both lists
    nums1_count = 0
    nums2_count = 0

    # Iterate through nums1 and count how many elements are in nums2
    for i in nums1:
        if i in nums2:
            nums1_count += 1

    # Iterate through nums2 and count how many elements are in nums1
    for i in nums2:
        if i in nums1:
            nums2_count += 1

    # Return the counts as a list
    return [nums1_count, nums2_count]



'Solution 2: '


def findIntersectionValues(nums1, nums2):
    
    """
    Finds the number of elements in nums1 that are also in nums2 and vice versa.

    :param nums1: List of integers.
    :param nums2: List of integers.
    :return: List of two integers [nums1_count, nums2_count].
    """
    # Convert nums2 to a set for O(1) average-time complexity lookups
    nums2_set = set(nums2)
    
    nums1_count = sum(1 for i in nums1 if i in nums2_set)
    nums2_count = sum(1 for i in nums2 if i in nums1)

    return [nums1_count, nums2_count]



'Solution 3: '


def findIntersectionValues(nums1, nums2):
    """
    Finds the number of elements in nums1 that are also in nums2 and vice versa.

    :param nums1: List of integers.
    :param nums2: List of integers.
    :return: List of two integers [nums1_count, nums2_count].
    """
    # Convert both lists to sets for efficient membership checking
    set_nums1 = set(nums1)
    set_nums2 = set(nums2)
    
    # Find the intersection of both sets, which are the common elements
    intersection = set_nums1 & set_nums2
    
    # Count how many elements in nums1 are in the intersection
    nums1_count = sum(1 for i in nums1 if i in intersection)
    
    # Count how many elements in nums2 are in the intersection
    nums2_count = sum(1 for i in nums2 if i in intersection)

    # Return the counts as a list
    return [nums1_count, nums2_count]
