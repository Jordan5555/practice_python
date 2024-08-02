"""

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.


Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
 

Constraints:

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109


"""

'Solution 1:'

def merge(nums1, m, nums2, n):

    # Initialize pointers for the end of the initialized parts of nums1 and nums2
    index1 = m - 1
    index2 = n - 1

    # Initialize the insert position at the end of the combined length of nums1
    insert_index = (m + n) - 1

    # Loop until all elements from nums2 are placed into nums1
    while index2 >= 0:

        # If there are elements left in nums1 and the current element of nums1 is greater than nums2
        if index1 >= 0 and nums1[index1] > nums2[index2]:

            # Place the current element of nums1 at the insert position
            nums1[insert_index] = nums1[index1]

            # Decrement the index for nums1 and the insert position
            index1 -= 1
            insert_index -= 1

        else:
            
            # Place the current element of nums2 at the insert position
            nums1[insert_index] = nums2[index2]

            # Decrement the index for nums2 and the insert position
            index2 -= 1
            insert_index -= 1

    # Return the merged array (this is actually not necessary as nums1 is modified in place)
    return nums1

print(merge([1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))



