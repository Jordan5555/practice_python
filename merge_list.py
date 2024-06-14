def merge(nums1, m, nums2, n):
    i = m - 1  # nums1's index (the actual nums)
    j = n - 1  # nums2's index
    k = m + n - 1  # nums1's index (the next filled position)

    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            k -= 1
            i -= 1
        else:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1

    return nums1

        
        
print(merge([1,2,3,0,0,0],3,[2,5,6],3))