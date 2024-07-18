"""

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000


"""

'Solution 1:'


def intersect(nums1, nums2):
    
    # Initialize an empty dictionary to store frequency of numbers in nums2
    nums2_dict = {}

    # Initialize an empty list to store the intersection elements
    out = []

    # Count frequencies of numbers in nums2 using a dictionary
    for num in nums2:
        
        nums2_dict[num] = nums2_dict.get(num, 0) + 1

    # Iterate through nums1 to find intersection elements
    for num in nums1:
        
        # Check if num is present in nums2_dict and has remaining occurrences
        if num in nums2_dict and nums2_dict[num] > 0:
            
            # Append num to out since it's part of the intersection
            out.append(num)

            # Decrease the count of num in nums2_dict to reflect usage
            nums2_dict[num] -= 1

    # Return the list containing the intersection elements
    return out

  


nums1 = [1,2,2,1]

nums2 = [2,2]

print(intersect(nums1, nums2))