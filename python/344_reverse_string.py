"""

Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
 

Constraints:

1 <= s.length <= 105
s[i] is a printable ascii character.

"""


'Solution 1:'

def reverseString(s):

    # Initialize left pointer at the beginning of the string
    left = 0

    # Initialize right pointer at the end of the string
    right = len(s) - 1

    # Loop until the pointers meet or cross each other
    while left <= right:

        # Swap characters at positions left and right
        s[left], s[right] = s[right], s[left]

        # Move left pointer to the right
        left += 1
        
        # Move right pointer to the left
        right -= 1
  
    # Return the modified string s with characters reversed in place
    return s



'Solution 2:'



def reverseString(s):

    # Iterate over the first half of the string
    for i in range(len(s) // 2):

        # Swap characters using Python's extended slicing and negative indexing
        s[i], s[~i] = s[~i], s[i]

    # Return the reversed string (although in Python, this is modifying the list in place)
    return s



