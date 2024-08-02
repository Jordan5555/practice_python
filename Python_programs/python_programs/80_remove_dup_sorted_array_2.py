"""


Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

 

Example 1:

Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
 

Constraints:

1 <= nums.length <= 3 * 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.


"""


'Problem same as 26'


'Solution 1: '


def func(nums):

    # Initialize the left pointer
    left = 0

    # Initialize the right pointer
    right = 1

    # Loop until the right pointer reaches the second to last element of the list
    while right < len(nums) - 1:

        # Check if the current element and the next two elements are the same
        if nums[left] == nums[right] == nums[right + 1]:

            # Remove the third element in the triplet
            nums.remove(nums[right + 1])

        else:

            # Move the left pointer to the right pointer
            left = right

            # Move the right pointer one step to the right
            right += 1

    # Return the modified list
    return nums



'Solution 2: '


def func(nums):
    
    # Initialize a pointer k to keep track of the position in the modified array
    k = 0

    # Iterate through each number in the input array
    for num in nums:

        # Check if we are at the start of the array or if the current number is not the same as the number two positions before it
        if k < 2 or num != nums[k - 2]:

            # If the above condition is met, place the current number at the k-th position of the array
            nums[k] = num

            # Increment k to move to the next position in the modified array
            k += 1

    # Return the modified part of the array up to the k-th position
    return nums[:k]




'Solution 3: '



def removeDuplicates(nums):

    # Initialize index i to 0
    i = 0
    
    # Iterate through the list 'nums' using a while loop
    while i < len(nums) - 2:
        
        # Check if the current element is equal to the second element
        if nums[i] == nums[i + 1] == nums[i+2]:
            
            # If duplicate found, remove the next element using pop()
            nums.pop(i + 2)
            
        else:
            # If no duplicate, move to the next element
            i += 1
    
    # Return the length of the modified 'nums' list
    return nums
